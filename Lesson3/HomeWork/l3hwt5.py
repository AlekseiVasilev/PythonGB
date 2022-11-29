# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
from typing import Optional


def give_int(input_string: str,
             min_num: Optional[int] = None) -> int:
    '''
    Gives integer number

    :param input_string: welcome to input
    :param min_num: minimum for number's value
    :return: int number
    '''

    while True:
        try:
            num = int(input(input_string))
            if min_num and num < min_num:
                print(f'Type number which value is {min_num} or bigger!')
                continue
            return num
        except ValueError:
            print("That's not a natural number.")


def neg_fibo_pos(number: int) -> list:
    '''
    Gives list with fibonacci(append)/negofibonacci(insert to 0 index) values.

    :param number: number of elements
    :return: list with fibonacci/negofibonacci values
    '''

    np_fibo = [0]
    fib1 = 0
    fib2 = 1
    neg = 1
    for i in range(1, number + 1):
        fib1, fib2 = fib2, fib1 + fib2
        np_fibo.append(fib1)
        np_fibo.insert(0, neg * fib1)
        neg *= -1
    return np_fibo


num = give_int("Type amount of Fibonacci's/Negafibonacci's elements: ", 1)
print(neg_fibo_pos(num))
