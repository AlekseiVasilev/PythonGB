# Following methods are used in 5 tasks of homework.
# So that's why i moved it "library"


from random import random, randint
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
            if min_num and num <= min_num:
                print(f'Type number bigger then {min_num}!')
                continue
            return num
        except ValueError:
            print("That's not a natural number.")


def random_list(listlen: int) -> list:
    '''
    Gives list with random values

    :param listlen: list's length
    :return: list with random values
    '''

    datalist = list()
    for i in range(listlen):
        datalist.append(randint(-10, 10))
    return datalist


def random_list_float(listlen: int) -> list:
    '''
    Gives list with random values

    :param listlen: list's length
    :return: list with random values
    '''

    datalist = list()
    for i in range(listlen):
        datalist.append(round(random() - randint(-10, 10), 4))
    return datalist
