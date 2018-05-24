# Прочитайте его и подсчитайте количество слов в тексте
from count_words import count_words

count_word = 0
with open('C:/Users/aatel/PycharmProjects/LearnPython/referat.txt', 'r', encoding='utf-8') as f:
    for line in f:
        count_word += int(count_words(line))
    print(count_word)