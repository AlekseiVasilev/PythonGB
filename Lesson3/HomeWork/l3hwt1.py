# 1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from gbfunctions import give_int, random_list


def summary_on_pos(datalist):
    '''
    Gives concatenation of elements on odd indexes

    :param datalist: list with elements
    :return: concatenation of elements on odd indexes
    '''

    summ = 0
    for i in range(1, len(datalist), 2):
        summ += datalist[i]
    return summ


size = give_int('Type value for length of the list: ', 1)
numbers = random_list(size)
print(numbers)
print(f'Summary is: {summary_on_pos(numbers)}')
