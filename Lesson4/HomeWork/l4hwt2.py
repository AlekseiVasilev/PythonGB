# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# in
# 54
# out
# [2, 3, 3, 3]

from math import sqrt


def simple_numbers(n):
    simples = [2]
    for i in range(3, n + 1, 2):
        for j in simples:
            if j * j - 1 > i:
                simples.append(i)
                break
            if (i % j == 0):
                break
        else:
            simples.append(i)
    return simples


def simple_factors(n, simples):
    factors = []
    i = 0
    while n != 1:
        if n % simples[i] == 0:
            n //= simples[i]
            factors.append(simples[i])
        else:
            i += 1
    return factors


num = int(input('Enter natural number N: '))
simp_nums = simple_numbers(num)
print(simple_factors(num, simp_nums))
