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
            return players_list, 1
        else:
            return exit('Very funny. Only positive number')
    except ValueError:
        return exit('Rly...how we start without people?!')


def master_choose():
    try:
        while True:
            mode = int(input('Do you want to be a Game Master, or destiny will choose? (1/2):'))
            if mode == -1:
                exit('So...bye-bye')
            elif mode == 1 or mode == 2:
                return mode
            else:
                print('Choose 1 or 2, or type "-1" to end the process.')
    except ValueError:
        exit('No-no-no...1 or 2 next time')


def game_algo(round_result, round_amount, start_position, game_mode):
    print('Start =', start_position)
    if game_mode == 1:
        try:
            master_count = int(input('Hmmm...how many steps do you want?\n'))
            if master_count <= 0:
                exit('How you wanna count with this value?! Type positive number next time!')
        except ValueError:
            exit('Facepalm...')
    else:
        master_count = randint(1, len(round_result))
    hash = []
    while master_count != 0:
        if start_position < len(round_result):
            round_result[start_position-1][1] += 1
            hash.append(start_position)
        else:
            start_position = 1
            round_result[start_position-1][1] += 1
            hash.append(start_position)
        start_position += 1
        master_count -= 1
    for i in range(len(round_result)):
        if round_result[i][0] not in hash:
            round_result[i][1] += 2
    print(round_result)
    print(start_position)
    round_result.pop(start_position-2)
    print(round_result)
    return round_result, start_position - 1


a, start = input_method()
game_mode = master_choose()
for i in range(len(a) - 1):
    a, start = game_algo(a, i + 1, start, game_mode)
    if len(a) > 1:
        print('\nNext round start in 3 seconds!\n------------------')
        sleep(3)
    else:
        exit(f'Our winner is Player #{a[0][0]}.\nYour jackpot is {a[0][1]}.000.000 $\nCongratulations!!!')
