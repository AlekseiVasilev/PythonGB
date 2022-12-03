# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


from gbfunctions import give_int
from typing import List


def simple_factors(n: int) -> List[int]:
    """
    Makes empty list, then add simple factors of n there, if factor isn't already in list.

    :param n: number[int] - natural number
    :return: list[int] - simple factors of n number
    """

    factors = []
    i = 2
    while n != 1:
        if n % i == 0:
            n //= i
            if i not in factors:
                factors.append(i)
        else:
            i += 1
    return factors


num = give_int('Enter natural number N: ', 1)
result = simple_factors(num)
print(f'Simple factors of {num}: {result}')
