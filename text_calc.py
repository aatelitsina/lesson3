import re
from calculate import calculate
def text_calculate(string):
    numbers = {'один':'1', 'два':'2', 'три':'3', 'четыре':'4', 'пять':'5', 'шесть':'6', 'семь':'7', 'восемь':'8', 'девять':'9', 'ноль':'0'}
    operators = {'плюс':'+','минус':'-','умножить':'*','делить':'/'}
    string = string.split()
    word_ind = 0
    num_string = ''
    while word_ind < len(string):
        if string[word_ind] in numbers:
            num_string =num_string + numbers[string[word_ind]]
        elif string[word_ind] in operators:
            num_string = num_string + operators[string[word_ind]]
        elif string[word_ind] == 'и' and word_ind-1 >= 0 and word_ind+1 < len(string) and  string[word_ind-1] in numbers  and string[word_ind +1] in numbers:
                num_string = num_string + '.'

        word_ind += 1
    return calculate(num_string)

# text_calculate('Сколько будет восемь и пять делить на два')


