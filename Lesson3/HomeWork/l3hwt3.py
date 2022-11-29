# 3. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from random import random, randint
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
        datalist.append(round(random() - randint(-10, 10), 4))
    return datalist


def max_min_fract(datalist):  # fractal part for negative number:
    max_fract = 0.0  # -5.9 = -6 + 0.1   fract_part = 0.1
    min_fract = 1.0
    for i in range(len(datalist)):
        fract_part = round(datalist[i] % 1, 4)
        if fract_part >= max_fract:
            max_fract = fract_part
        if fract_part <= min_fract:
            min_fract = fract_part
    print('Max fractal part:', max_fract)
    print('Max fractal part:', min_fract)
    summ = round(max_fract - min_fract, 4)
    return summ


size = give_int('Type value for length of the list: ', 1)
numbers = random_list(size)
print(numbers)
print(f'Difference is: {max_min_fract(numbers)}')
