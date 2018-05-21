from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
import settings
import string
import re

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

PROXY = {'proxy_url': 'socks5://u0k12.tgproxy.me:1080', 'urllib3_proxy_kwargs': {'username': 'telegram', 'password': 'telegram'}}

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text('меня нет')


def start_planet(bot, update):
    text = 'Напечатайте планету на английском'
    print(text)
    update.message.reply_text(text)


def where_planet(bot, update):
    planet_text = update.message.text
    print(planet_text)
    if planet_text == 'Mercury':
        planet = ephem.Mercury()
    elif planet_text == 'Venus':
        planet = ephem.Venus()
    elif planet_text == 'Mars':
        planet = ephem.Mars()
    elif planet_text == 'Jupiter':
        planet = ephem.Jupiter()
    elif planet_text == 'Saturn':
        planet = ephem.Saturn()
    elif planet_text == 'Uranus':
        planet = ephem.Uranus()
    elif planet_text == 'Neptune':
        planet = ephem.Neptune()
    elif planet_text == 'Pluto':
        planet = ephem.Pluto()
    elif planet_text == 'Sun':
        planet = ephem.Sun()
    elif planet_text == 'Moon':
        planet = ephem.Moon()
    else:
        update.message.reply_text('Я не знаю такой планеты')
        return

    planet.compute()
    update.message.reply_text(ephem.constellation(planet))

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

def call_calculate(bot, update):
     text = 'Напишите уравнение, заканчивающееся знаком ='
     update.message.reply_text(text)
     equation = update.message.text
     try:
         numbers = re.split(r'[+-/\*]', equation)
         sign = re.findall(r'[\+-/\*]', equation)
         for numb in range(len(numbers)):
             result = int(numbers[numb])
             numb += 1
             if '+' in sign:
                 result += int(numbers[numb])
                 break
             elif '-' in sign:
                 result -= int(numbers[numb])
                 break
             elif '/' in sign:
                 result = result / int(numbers[numb])
                 break
             elif '*' in sign:
                 result *= int(numbers[numb])
                 break
     except ZeroDivisionError:
         print('Деление на 0!!!')
     except (SyntaxError, ValueError):
         print('Введите числа')
     else:
         update.message.reply_text(result)



def main():
    mybot = Updater(settings.TELEGRAM_API_KEY, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", start_planet))
    dp.add_handler(CommandHandler("wordcount", print_word))
    dp.add_handler(CommandHandler("calculate", call_calculate))
    # dp.add_handler(MessageHandler(Filters.text, call_calculate))
    # dp.add_handler(MessageHandler(Filters.text, how_match))
    # dp.add_handler(MessageHandler(Filters.text, where_planet))
    # dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()
