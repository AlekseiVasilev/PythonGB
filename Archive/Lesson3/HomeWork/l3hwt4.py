# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from random import random, randint


def random_list(listlen):
    datalist = list()
    for i in range(listlen):
        datalist.append(round(random() - randint(-10, 11), 2))
    return datalist


def max_min_fract(datalist):  # fractal part for negative number:
    max_fract = 0.0  # -5.9 = -6 + 0.1   fract_part = 0.1
    min_fract = 1.0
    for i in range(len(datalist)):
        fract_part = round(datalist[i] % 1, 2)
        if fract_part >= max_fract:
            max_fract = fract_part
        if fract_part <= min_fract:
            min_fract = fract_part
    summ = round(max_fract - min_fract, 2)
    return summ


size = int(input('Type value for length of the list: '))
numbers = random_list(size)
print(numbers)
print(f'Difference is: {max_min_fract(numbers)}')
