# 4 - По кругу стоят n человек. Ведущий посчитал m человек по кругу, начиная с первого.
# При этом каждый из тех, кто участвовал в этом счете, получил по одной монете, остальные получили по две монеты.
# Далее человек, на котором остановился счет, отдает все свои монеты следующему по счету человеку,
# а сам выбывает из круга. Процесс продолжается с места остановки аналогичным образом до последнего человека в круге.
# Составьте алгоритм, который проводит эту игру.
# Если хотите делать паузы, то импортируйте библиотеку time и используйте оттуда функцию sleep.
# Определите номер этого человека и количество монет, которые оказались у него в конце игры.
from random import randint
from time import sleep


def input_method():
    try:
        players_number = int(input('Type value for players number: '))
        if players_number > 0:
            players_list = [[i, 0] for i in range(1, players_number + 1)]
            return players_list
        else:
            return exit('Value is incorrect')
    except ValueError:
        return exit('Value is incorrect')

def game_algo(round_result, round_amount):
    master_count = randint(0, len(round_result) - 1)
    print(f'One-two...i choose you #{round_result[master_count][0]}! WHOAAAHHAHAH')
    for game_breakpoint in range(master_count + 1):
        coins_amount = 1
        round_result[game_breakpoint][1] += coins_amount
    for game_breakpoint in range(master_count + 1, len(round_result)):
        coins_amount = 2
        round_result[game_breakpoint][1] += coins_amount
    print(f'Results after {round_amount} round:')
    for i in round_result:
        print(f'Player #{i[0]} have coins = {i[1]}')
    try:
        round_result[master_count + 1][1] += round_result[master_count][1]
    except IndexError:
        round_result[0][1] += round_result[master_count][1]
    print(f'\n------------------\nPlayer #{round_result[master_count][0]} is out!\n------------------\n')
    round_result.pop(master_count)

    for i in round_result:
        print(f'Player #{i[0]} have coins = {i[1]}')
    return round_result

a = input_method()
for i in range(len(a) - 1):
    a = game_algo(a, i+1)
    if len(a) > 1:
        print('\nNext round start in 3 seconds!\n------------------')
        sleep(3)
    else:
        exit(f'Our winner is Player #{a[0][0]}.\nYour jackpot is {a[0][1]}.000.000 $\nCongratulations!!!')

