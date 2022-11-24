# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# in
# 54
# out
# [2, 3, 3, 3]

from math import sqrt


def simple_factors(n):
    factors = []
    i = 2
    while n != 1:
        if n % i == 0:
            n //= i
            factors.append(i)
        else:
            i += 1
    return factors


num = int(input('Enter natural number N: '))
print(simple_factors(num))
