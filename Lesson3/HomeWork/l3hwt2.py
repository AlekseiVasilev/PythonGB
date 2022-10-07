# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]

from random import randint


def random_list(listlen):
    datalist = list()
    for i in range(listlen):
        datalist.append(randint(-10, 11))
    return datalist


def pair_mult(datalist):
    multiple = list()
    for i in range(len(datalist) // 2):
        multiple.append(datalist[i] * datalist[-1 - i])
    return multiple


size = int(input('Type value for length of the list: '))
numbers = random_list(size)
print(numbers)
print(f"Pair's multiplication is: {pair_mult(numbers)}")
