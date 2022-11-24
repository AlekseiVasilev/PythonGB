# 3. Задайте два числа. Напишите программу, которая найдёт
# НОК (наименьшее общее кратное) этих двух чисел.

from math import gcd


def nok(a, b):
    return (a * b) // gcd(a, b)


first = int(input('Type value for the first number: '))
second = int(input('Type value for the first number: '))
print(nok(first, second))
