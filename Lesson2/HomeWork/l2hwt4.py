# 4. Напишите программу, которая принимает на вход 2 числа.
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

pos_first = int(input('Enter first position: '))
pos_second = int(input('Enter second position: '))
num = int(input('Enter number of elements: '))
if num * 2 + 1 < pos_first or num * 2 + 1 < pos_second:
    quit(print('Incorrect number of elements. Restart the programm'))
elif pos_first < 1 or pos_second < 1:
    quit(print('Incorrect positions. Restart the programm'))
elements = list(range(-num, num + 1, 1))
print(elements)
result = elements[pos_first - 1] * elements[pos_second - 1]
print(result)
