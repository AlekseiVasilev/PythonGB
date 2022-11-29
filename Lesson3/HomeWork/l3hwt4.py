# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
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


def int_to_binary(number: int) -> str:
    '''
    Gives binary number from dec number as result.
    Makes reversed list which contains reminder of a division by 2, until number became zero.
    Then makes string, united this values.

    :param number: number to make binary
    :return: string with binary value
    '''

    binary = []
    while number // 2 != 0:
        binary.insert(0, number % 2)
        number //= 2
    binary.insert(0, number)
    result = "".join(map(str, binary))
    return result


num = give_int('Enter natural number: ', 1)
binary = int_to_binary(num)
print(f'{num} == 0b{binary}')
