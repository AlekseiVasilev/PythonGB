# 1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from random import randint
from typing import Optional


def give_int(input_string: str,
             min_num: Optional[int] = None) -> int:
    '''
    Gives integer number

    :param input_string: welcome to input
    :param min_num: minimum for number's value
    :return: int number
    '''

    while True:
        try:
            num = int(input(input_string))
            if min_num and num <= min_num:
                print(f'Type number bigger then {min_num}!')
                continue
            return num
        except ValueError:
            print("That's not a natural number.")


def random_list(listlen):
    '''
    Gives list with random values

    :param listlen: list's length
    :return: list with random values
    '''

    datalist = list()
    for i in range(listlen):
        datalist.append(randint(-10, 10))
    return datalist


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
