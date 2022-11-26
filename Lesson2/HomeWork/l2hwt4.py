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
            exit('Very funny. Only positive number')
    except ValueError:
        exit('Rly...how we start without people?!')


def master_choose():
    try:
        mode = int(input('Do you want to be a Game Master, or destiny will choose? (1/2):'))
        if mode == 1 or mode == 2:
            return mode
        else:
            exit("Choose 1 or 2...it's not so hard, isn't it?")
    except ValueError:
        exit('No-no-no...1 or 2 next time')


def game_algo(round_result, round_amount, start_position, game_mode):
    if game_mode == 1:
        try:
            master_count = int(input('Hmmm...how many steps do you want?\n'))
            if master_count <= 0:
                exit('How you wanna count with this value?! Type positive number next time!')
            if master_count > len(round_result):
                print("Uhhh...i'm tired, you can't count more then pepople's amount, so")
                master_count = len(round_result)
        except ValueError:
            exit('Facepalm...')
    else:
        master_count = randint(1, len(round_result))
    hash = []
    while master_count != 0:
        if start_position <= len(round_result):
            round_result[start_position - 1][1] += 1
            hash.append(round_result[start_position - 1][0])
        else:
            start_position = 1
            round_result[start_position - 1][1] += 1
            hash.append(round_result[start_position - 1][0])
        start_position += 1
        master_count -= 1
    for i in range(len(round_result)):
        if round_result[i][0] not in hash:
            round_result[i][1] += 2
            hash.append(i)
    print(f"Let's count the coins after {round_amount} round before elimination...")
    for i in range(len(round_result)):
        print(f'Player #{round_result[i][0]}: {round_result[i][1]} coins')
    try:
        round_result[start_position - 1][1] += round_result[start_position - 2][1]
    except IndexError:
        round_result[0][1] += round_result[start_position - 2][1]
    print(f'\n------------\nWhoaahah...PLAYER #{round_result[start_position - 2][0]}! I CHOOSE YOU!\n------------\n')
    round_result.pop(start_position - 2)
    print(f"Let's count the coins after elimination...")
    for i in range(len(round_result)):
        print(f'Player #{round_result[i][0]}: {round_result[i][1]} coins')
    return round_result, start_position - 1


game_data, start = input_method()
game_mode = master_choose()
for i in range(len(game_data) - 1):
    a, start = game_algo(game_data, i + 1, start, game_mode)
    if len(a) > 1:
        print('\nNext round start in 3 seconds!\n------------------')
        sleep(3)
print(f'Our winner is Player #{game_data[0][0]}.\nYour jackpot is {game_data[0][1]}.000.000 $\nCongratulations!!!')
