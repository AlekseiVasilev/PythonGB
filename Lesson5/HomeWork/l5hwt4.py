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


def cortege_list_creator(lang: List[str] = ['python', 'c#', 'c++', 'rust', 'kotlin', 'java', 'swift'],
                         numbers: List[int] = [1, 2, 3, 4, 5, 6, 7]) -> List:
    lang = list(map(str.upper, lang))
    cortege = list(zip(numbers, lang))
    return cortege


def ord_summary(cort_item: str) -> int:
    symbol_summary = 0
    for i in cort_item:
        symbol_summary += ord(i)
    return symbol_summary


def rampam(data: List) -> List:
    new_data = []
    for i in range(len(data)):
        if not ord_summary(data[i][1]) % data[i][0]:
            new_data.append((ord_summary(data[i][1]), data[i][1]))
    return new_data


print(rampam(cortege_list_creator()))
