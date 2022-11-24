# 2. Создайте список, в который попадают числа,
# описывающие возрастающую последовательность.
# Порядок элементов менять нельзя.

from secrets import choice
from random import sample


def create_list():
    rnd_ls = list(sample(range(30), 7))
    return rnd_ls


def subseq_elem(ls, pos):
    ss_el = []
    ss_el.append(ls[pos])
    max = ls[pos]
    for i in range(pos, len(ls) - 1):
        if max < ls[i + 1]:
            max = ls[i + 1]
            ss_el.append(max)
    if len(ss_el) < 2:
        return -1
    else:
        return ss_el


def subseq_ls(ls):
    ss_ls = []
    for i in range(len(ls)):
        temp = subseq_elem(ls, i)
        if temp != -1:
            ss_ls.append(temp)
    return ss_ls


data = create_list()
print(data)
print(subseq_ls(data))
