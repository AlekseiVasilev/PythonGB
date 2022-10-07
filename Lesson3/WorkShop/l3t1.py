# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая определит, присутствует ли в заданном списке число,
# полученное от пользователя

from random import sample


def datalist(size):
    data = list(range(1000))
    return sample(data, size)


def inlist(number, data):
    if number in data:
        return True
    else:
        return False


listsize = int(input('Enter size of list: '))
num = int(input('Enter the number to find: '))
if inlist(num, datalist(listsize)):
    print(f'Number {num} is in random list')
else:
    print(f'Number is not on list')
