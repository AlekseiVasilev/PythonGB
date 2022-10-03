# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

power = int(input('Type amount of elements: '))
result = [power - 1]
for i in range(power):
    print((-3) ** i, end=' ')
