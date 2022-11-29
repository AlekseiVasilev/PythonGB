# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.


from gbfunctions import give_int


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
