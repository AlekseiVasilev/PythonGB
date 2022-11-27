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
            print('Very funny. Only positive number')
            input_method()
    except ValueError:
        print('Rly...how we start without people?!')
        input_method()


def master_choose():
    try:
        mode = int(input('Do you want to be a Game Master, or destiny will choose? (1/2):'))
        if mode == 1 or mode == 2:
            return mode
        else:
            print("If this is so hard, i'll choose myself WHOAHAHAAH!!")
            mode = 2
            return mode
    except ValueError:
        print('I see...now, destiny in my hands!')
        mode = 2
        return mode


def turn_exception(rnd_result):
    try:
        mst_count = int(input('Hmmm...how many steps do you want?\n'))
        if mst_count <= 0 or mst_count > len(rnd_result):
            print('How you wanna count with this value?! Type positive number next time!')
            mst_count = randint(1, len(rnd_result))
        return mst_count
    except ValueError:
        print('Facepalm...')
        mst_count = randint(1, len(rnd_result))
        return mst_count


def game_algo(round_result, round_amount, start_position, game_mode):
    if game_mode == 1:
        master_count = turn_exception(round_result)
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

try:
    game_data, start = input_method()
except TypeError:
    print('Something goes wrong, try again please')
    game_data, start = input_method()
game_mode = master_choose()
for i in range(len(game_data) - 1):
    a, start = game_algo(game_data, i + 1, start, game_mode)
    if len(a) > 1:
        print('\nNext round start in 3 seconds!\n------------------')
        sleep(3)
print(f'Our winner is Player #{game_data[0][0]}.\nYour jackpot is {game_data[0][1]}.000.000 $\nCongratulations!!!')
