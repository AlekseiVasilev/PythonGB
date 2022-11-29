# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from gbfunctions import give_int, random_list


def pair_mult(datalist):
    '''
    Gives multiplication of elements on opposite indexes

    :param datalist: list with elements
    :return: list with multiplication of elements on opposite indexes
    '''

    multiple = list()
    for i in range(len(datalist) // 2 + len(datalist) % 2):
        multiple.append(datalist[i] * datalist[-1 - i])
    return multiple


size = give_int('Type value for length of the list: ', 1)
numbers = random_list(size)
print(numbers)
print(f"Pair's multiplication is: {pair_mult(numbers)}")
