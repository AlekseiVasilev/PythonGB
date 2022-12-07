# 2- Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from gbfunctions import give_int
from typing import List
from random import randint


def player_logic(player_name: str, turn_limitation: int = 28, num: int = 2021) -> int:
    """
    Description for human logic. Just input number and couple verifications

    :param player_name: describes itself
    :param turn_limitation: maximum sweets you can take for 1 turn
    :param num: sweets remaining
    :return: amount of sweets was taken
    """

    sweet = 0
    while not 0 < sweet <= turn_limitation:
        sweet = give_int(f'{player_name}, how many sweets do you want to take?\n>> ', 1)
        if sweet > turn_limitation:
            print(f"You can't take more than {turn_limitation}")
        elif sweet > num:
            print(f"You can't take more than {num}")

    return sweet


def bot_logic(player_name: str, turn_limitation: int = 28, num: int = 2021) -> int:
    """
    Description for bot logic. It tries to leave as many sweets as you can't take on
    last turn. Or if he is on low level - just randint for luck!

    :param player_name: describes itself
    :param turn_limitation: maximum sweets bot can take for 1 turn
    :param num: sweets remaining
    :return: amount of sweets was taken
    """

    sweet = 0
    if player_name == 'Master Yoda':
        if num <= turn_limitation:
            sweet = num
        else:
            if num % turn_limitation > 1:
                sweet = num % turn_limitation - 1
            else:
                sweet = turn_limitation - num % turn_limitation + 1
    elif player_name == 'Jar Jar Binks':
        if num <= turn_limitation:
            sweet = num
        else:
            sweet = randint(1, 28)
    print(f'{player_name} takes {sweet} sweets!')
    return sweet


def vs_algo(player_tuple: List[tuple], number: int = 2021) -> None:
    """
    Just turn maker for this game. Randomly choice who will be first.
    Used for both modes, as player_vs_player and player_vs_bot

    :param player_tuple: players list with number, name and status
    :param number: sweets remaining
    :return: info to console
    """

    first_turn = randint(0, 1)
    while number != 0:
        if player_tuple[first_turn][2] == 'man':
            sweet_amount = player_logic(player_name=player_tuple[first_turn][1], num=number)
        elif player_tuple[first_turn][2] == 'bot':
            sweet_amount = bot_logic(player_name=player_tuple[first_turn][1], num=number)
        number -= sweet_amount
        print(f'{number} of sweets remains!\n')
        if number <= 0:
            exit(print(f'{player_tuple[first_turn][1]} WIN!\nCongratulations!'))
        else:
            if first_turn:
                first_turn = 0
            else:
                first_turn = 1


def menu_input() -> None:
    """
    Creates console menu for user.
    Creates players list and give it to game master algorithm

    :return: info to console
    """

    while True:
        print('Type "1" if you want to play in 2 player mode')
        print('Type "2" if you want to play vs bot')
        print('Type "-1" if you want to exit')
        num = input('What operation do you want to do?: ')
        if num == '1':
            pl_list = [(0, input('Type first player name:\n>> '), 'man'),
                       (1, input('Type second player name:\n>> '), 'man')]
            vs_algo(pl_list)
        elif num == '2':
            level = 0
            while level not in (1, 2):
                level = give_int('Choose COM level\n'
                                 '1. Chuck Norris\n'
                                 '2. Ne ponimaet wto proishodit...\n'
                                 '>> ', 1)
                if level > 2:
                    print(f"Come on! 1 is minimum, 2 is maximum..It's not that hard.")
            if level == 1:
                pl_list = [(0, input('Type first player name:\n>> '), 'man'),
                           (1, 'Master Yoda', 'bot')]
            else:
                pl_list = [(0, input('Type first player name:\n>> '), 'man'),
                           (1, 'Jar Jar Binks', 'bot')]
            vs_algo(pl_list)
        elif num == '-1':
            return exit(print("Bye-bye"))
        else:
            print("Incorrect value, try again!")


menu_input()
