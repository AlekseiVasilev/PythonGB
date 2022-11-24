# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
# Напишите программу, которая определит индекс второго вхождения строки в списке
# либо сообщит, что её нет

from random import choices


def datalist(size, word):
    massive = []
    for i in range(size):
        massive.append("".join(choices(word, k=2)))
    return massive


def finder(data, what_find):
    count = 0
    for i in range(len(data)):
        if what_find == data[i]:
            count += 1
            if count == 2:
                return i
    return -1


database = datalist(int(input("Enter number of words: ")), "xy")
print(database)
print(finder(database, "xx"))
