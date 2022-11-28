# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['gfh5', 'gfh2', '67', 'jy32', '3put'] - ищем 32 - находим по индексу 3

def input_list():
    data = input('Введите значения в списке через пробел:\n').split(" ")
    return data


def find_value(data_list):
    what_find = input('Кого ищем то?\n')
    result = []
    for i in range(len(data_list)):
        if what_find in data_list[i]:
            result.append(i)
    return result if result else 'None'


elements = input_list()
result_list = find_value(elements)
print(result_list)
