# 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

from random import randint


def random_list(listlen):
    datalist = list()
    for i in range(listlen):
        datalist.append(randint(0, 5))
    return datalist


def alone_objects(lst):
    count = 0
    new_lst = []
    for i in lst:
        for j in range(len(lst)):
            if lst[j] == i:
                count += 1
        if count == 1:
            new_lst.append(i)
        count = 0
    return new_lst


size = int(input("Enter the length of the list: "))
sample_lst = random_list(size)
print(sample_lst)
print(alone_objects(sample_lst))
