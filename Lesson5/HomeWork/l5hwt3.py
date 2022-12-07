# Создайте программу для игры в ""Крестики-нолики"". Для определения победы вам может пригодиться функция filter.
# Проверяйте победу после каждого хода, фильтруя столбцы, строки и диагонали по знаку хода

from typing import List
from gbfunctions import give_int


def field_creator(turns_list: List):
    """
    Draw field for game

    :param turns_list: coordinates of field's cell
    :return: field to console
    """

    print("---------------")
    print(f"  {turns_list[0]}    {turns_list[1]}    {turns_list[2]}  ")
    print(f"  {turns_list[3]}    {turns_list[4]}    {turns_list[5]}  ")
    print(f"  {turns_list[6]}    {turns_list[7]}    {turns_list[8]}  ")
    print("---------------")


def turn_maker(player: List, turns_list: List) -> None:
    """
    Algorithm for game

    :param player: list with players number and name
    :param turns_list: list with field's cells
    :return: some info to console about turn
    """

    pl = player[0]
    for i in range(len(turns_list) - 1):
        new_turn = 10
        while new_turn > 9 or turns_list[new_turn - 1] in ('X', 'O'):
            new_turn = give_int(f"{pl[1]}, please, choose cell for your turn: ", 1)
            if new_turn > 9 or turns_list[new_turn - 1] in ('X', 'O'):
                print("You can't place your mark there!\n")
        if pl == player[0]:
            turns_list[new_turn - 1] = "X"
            field_creator(turns_list)
            if i >= 4:
                win_condition(turns_list, player[0])
            pl = player[1]
        else:
            turns_list[new_turn - 1] = "O"
            field_creator(turns_list)
            if i >= 4:
                win_condition(turns_list, player[1])
            pl = player[0]


def win_condition(turns_list: List, player: List) -> None:
    """
    Checks win condition and returns info about success

    :param turns_list: list with field's cells
    :param player: list with players number and name
    :return:
    """

    if turns_list[0] == turns_list[1] == turns_list[2] \
            or turns_list[3] == turns_list[4] == turns_list[5] \
            or turns_list[6] == turns_list[7] == turns_list[8] \
            or turns_list[0] == turns_list[3] == turns_list[6] \
            or turns_list[1] == turns_list[4] == turns_list[7] \
            or turns_list[2] == turns_list[5] == turns_list[8] \
            or turns_list[0] == turns_list[4] == turns_list[8] \
            or turns_list[2] == turns_list[4] == turns_list[6]:
        return exit(print(f"Congratulations, {player[1]} win!"))
    else:
        return


turn = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player1 = input("Enter first player name: ")
player2 = input("Enter second player name: ")
players = [[1, player1], [2, player2]]
field_creator(turn)
turn_maker(players, turn)
