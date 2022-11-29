# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

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


def pair_mult(datalist):
    multiple = list()
    for i in range(len(datalist) // 2):
        multiple.append(datalist[i] * datalist[-1 - i])
    if len(datalist) % 2 != 0:
        multiple.append(datalist[len(datalist) // 2] ** 2)
    return multiple


size = give_int('Type value for length of the list: ', 1)
numbers = random_list(size)
print(numbers)
print(f"Pair's multiplication is: {pair_mult(numbers)}")
