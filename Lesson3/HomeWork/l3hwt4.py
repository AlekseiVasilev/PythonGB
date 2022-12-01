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
    while number != 0:
        binary.insert(0, number % 2)
        number //= 2
    result = "".join(map(str, binary))  # 0b1010101010   [1, 1, 0, 0] .... 1 1 0 0
    return result


num = give_int('Enter natural number: ', 1)
binary = int_to_binary(num)
print(f'{num} == 0b{binary}')
print(int(binary, base=2))
