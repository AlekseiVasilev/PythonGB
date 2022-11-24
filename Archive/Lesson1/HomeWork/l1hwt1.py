# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day_number = ""
while not day_number.isdigit():
    day_number = input('Enter day number: ')
    if day_number.isdigit():
        day_number = int(day_number)
        if day_number < 1 or day_number > 7:
            day_number = ""
            print('Value is incorrect\nIf you want to exit the program then type "exit"')
        else:
            break
    elif day_number == "exit":
        exit('Bye-bye')
    else:
        print('Value is incorrect\nIf you want to exit the program then type "exit"')

if day_number in range(6, 8):
    print("It's a weekend, let's party!")
else:
    print("Boooriiiing, it's not a weekend")
