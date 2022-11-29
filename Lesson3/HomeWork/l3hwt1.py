# 1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from random import randint
from typing import Optional


def give_int(input_string: str,
             min_num: Optional[int] = None) -> int:
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
    datalist = list()
    for i in range(listlen):
        datalist.append(randint(-10, 10))
    return datalist


def summary_on_pos(datalist):
    summ = 0
    for i in range(1, len(datalist), 2):
        summ += datalist[i]
    return summ


size = give_int('Type value for length of the list: ', 1)
numbers = random_list(size)
print(numbers)
print(f'Summary is: {summary_on_pos(numbers)}')
