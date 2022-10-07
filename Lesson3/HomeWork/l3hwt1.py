# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

from random import randint


def random_list(listlen):
    datalist = list()
    for i in range(listlen):
        datalist.append(randint(-10, 11))
    return datalist


def summary_on_pos(datalist):
    summ = 0
    for i in range(0, len(datalist), 2):
        summ += datalist[i]
    return summ


size = int(input('Type value for length of the list: '))
numbers = random_list(size)
print(numbers)
print(f'Summary is: {summary_on_pos(numbers)}')
