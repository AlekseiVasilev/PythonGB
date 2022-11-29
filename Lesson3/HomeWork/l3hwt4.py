# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
from typing import Optional


def give_int(input_string: str,
             min_num: Optional[int] = None) -> int:
    while True:
        try:
            num = int(input(input_string))
            if min_num and num < min_num:
                print(f'Type number which value is {min_num} or bigger!')
                continue
            return num
        except ValueError:
            print("That's not a natural number.")


def int_to_binary(number):
    binary = []
    while number // 2 != 0:
        binary.insert(0, number % 2)
        number //= 2
    binary.insert(0, number)
    return binary


num = give_int('Enter natural number: ', 1)
print("".join(map(str, int_to_binary(num))))
