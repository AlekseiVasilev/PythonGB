# 4-Создайте два списка — один с названиями языков программирования, другой — с их нумерацией.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей,
# состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая (обязательно используйте tuple unpacking) — которая отфильтрует этот список следующим образом:
# если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже,
# то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется.
# Суммой очков называется сложение порядковых номеров букв в слове.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком

from typing import List


def cortege_list_creator(lang=None,
                         numbers=None) -> List[tuple[int, str]]:
    """
    Creates list with tuple[int, str] on lang and numbers zip.

    :param lang: list with language naming
    :param numbers: list with numbers
    :return: list with tuple[int, str]
    """

    if lang is None:
        lang = ['python', 'c#', 'c++', 'rust', 'kotlin', 'java', 'swift']
    if numbers is None:
        numbers = [1, 2, 3, 4, 5, 6, 7]
    lang = list(map(str.upper, lang))
    cortege = list(zip(numbers, lang))
    return cortege


def ord_summary(cort_item: tuple[str]) -> int:
    """
    Concatenation of all letters at 1 index of tuple

    :param cort_item: element of tuple on 1 index
    :return: int
    """

    symbol_summary = 0
    for i in cort_item:
        symbol_summary += ord(i)
    return symbol_summary


def filter_data(data: List) -> tuple[List[tuple[int, str]], int]:
    """
    Generates list with tuples, where 1 index ord_summary divides
    without reminder on it's number at 0 index.

    :param data: list with tuples
    :return: result list and all letters ord summary
    """

    # task example said, that 1 can't be divider...If not, just del this 1 in range
    data = [(ord_summary(data[i][1]), data[i][1]) for i in range(1, len(data))
            if not ord_summary(data[i][1]) % data[i][0]]
    elem_ord_sum = 0
    for i in data:
        elem_ord_sum += i[0]
    return data, elem_ord_sum


data_list = cortege_list_creator()
result = filter_data(data_list)
print(f'Result list with tuples: {result[0]}\nSummary of numbers: {result[1]}')
