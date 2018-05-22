import re
from calculate import calculate
string = 'сколько будет пять делить на один'
numbers = {'один':'1', 'два':'2', 'три':'3', 'четыре':'4', 'пять':'5', 'шесть':'6', 'семь':'7', 'восемь':'8', 'девять':'9', 'ноль':'0'}
operators = {'плюс':'+','минус':'-','умножить':'*','делить':'/'}
string = 'сколько будет три минус два'.replace('сколько будет ','').split()
print(string)
word_ind = 0
num_string = ''
while word_ind < len(string):
    if string[word_ind] in numbers:
        num_string =num_string + numbers[string[word_ind]]
    elif string[word_ind] in operators:
        num_string = num_string + operators[string[word_ind]]
    word_ind += 1
print(calculate(num_string))



