# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
#
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

from random import sample


def create_line(num):
    rand_string = ''
    for i in range(num - 1):
        rand_string += ''.join(sample("абв", 3)) + " "
    rand_string += ''.join(sample("абв", 3))
    return rand_string


def cut_keyword(txt, word):
    data_list = txt.split()
    i = 0
    while i < len(data_list):
        if data_list[i] == word:
            data_list.remove(data_list[i])
        else:
            i += 1
    result_string = ' '.join(data_list)
    return result_string


def input_meth():
    temp = 0
    while temp < 1:
        temp = int(input('Enter the number of words: '))
        if temp < 1:
            print('Incorrect data, try again')
    return temp


line = create_line(input_meth())
print(f'Start string is: {line}')
print(f"Result string is: {cut_keyword(line, 'абв')}")
