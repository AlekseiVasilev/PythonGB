# 2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:
#
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3

def input_list():
    data = input('Введите значения в списке через пробел:\n').split(" ")
    return data


def find_value(data_list):
    what_find = input('Кого ищем то?\n')
    count = 0
    for i in range(len(data_list)):
        if what_find in data_list[i]:
            count += 1
            if count == 2:
                return f'Индекс второго вхождения - {i}, а позиция - {i + 1}'
    else:
        return '2 раз не приходило, а может и первого раза не было, мы не в курсе'


elements = input_list()
result = find_value(elements)
print(result)
