# 1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.
# Пример:
# Пугать ты галок пугай => заданная строка "пугай" => Пугать ты галок

def cut_string(input_string: str) -> str:
    """
    Splits input string by space for words,
    then making new list with words that not contains 'to cut' string
    and put it to new string

    :param input_string: string from user
    :return: result string
    """

    to_cut = input('Type string you want to remove:\n>> ')
    result_list = [i for i in input_string.split() if to_cut not in i]
    return ' '.join(result_list)


result = cut_string(input('Type some text:\n>>'))
print(result)
