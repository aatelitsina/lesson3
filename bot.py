from calculate import calculate
from text_calc import text_calculate
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
import logging
import ephem
import settings
import string
import re

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
         'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text('меня нет')


# def start_planet(bot, update):
#     text = 'Напечатайте планету на английском'
#     update.message.reply_text(text)


planets = {
  'Mercury':ephem.Mercury(),
  'Venus':ephem.Venus(),
  'Mars':ephem.Mars(),
  'Jupiter':ephem.Jupiter(),
  'Saturn':ephem.Saturn(),
  'Uranus': ephem.Uranus(),
  'Neptune': ephem.Neptune(),
  'Pluto': ephem.Pluto(),
  'Sun': ephem.Sun(),
  'Moon': ephem.Moon(),
}
    
def where_planet(bot, update):
    planet = update.message.text
    print(planet)
    if planet not in planets.keys():
        update.message.reply_text('Я не знаю такой планеты')
        return
    else:
      planets[planet].compute()
      update.message.reply_text(ephem.constellation(planets[planet]))


def print_word(bot, update):
    text = 'Напечатайте фразу'
    print(text)
    update.message.reply_text(text)


def count_words(bot, update):
    phrase = update.message.text
    for wrd in string.punctuation:
        phrase = phrase.replace(wrd, '')
    words = str(len(phrase.split())) + ' кло-во слов во фразе'
    update.message.reply_text(words)


q_equation = ""


def call_calculate(bot, update):
    equation = update.message.text.replace('/calculate', '').strip()
    if equation == "":
        q_equation = ""
        custom_keyboard = [['7', '8', '9', '*'],
                           ['4', '5', '6', '-'],
                           ['1', '2', '3', '+'],
                           [',', '0', '=', '/']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        bot.send_message(chat_id=update.message.chat_id, text="Калькулятор", reply_markup=reply_markup)
        return

    update.message.reply_text(calculate(equation))


def auto_calculate(bot, update):
    if update.message.text.startswith('Когда ближайшее полнолуние после'):
        date_pol = re.search('\d{4}-\d{2}-\d{2}',update.message.text)
        if date_pol is None:
            update.message.reply_text('Введите дату формата гггг-мм-дд')
        else:
            date_pol = date_pol.group(0)
            date_pol = ephem.next_full_moon(date_pol)
            update.message.reply_text("{}".format(date_pol))
        return

    global q_equation
    if update.message.text != '=':
        q_equation = q_equation + update.message.text
    else:
        reply_markup = telegram.ReplyKeyboardRemove()
        bot.send_message(chat_id=update.message.chat_id, text=calculate(q_equation), reply_markup=reply_markup)


def text_calc(bot, update):
    statment = update.message.text.replace('/text_calc', '').strip()
    update.message.reply_text(text_calculate(statment))


def main():
    mybot = Updater(settings.TELEGRAM_API_KEY, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", where_planet))
    dp.add_handler(CommandHandler("wordcount", print_word))
    dp.add_handler(CommandHandler("calculate", call_calculate))
    dp.add_handler(CommandHandler("text_calc", text_calc))
    dp.add_handler(MessageHandler(Filters.text, auto_calculate))
    # dp.add_handler(MessageHandler(Filters.text, count_words))
    # dp.add_handler(MessageHandler(Filters.text, where_planet))
    # dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
