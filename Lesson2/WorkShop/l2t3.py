# 3. Напишите программу, в которой пользователь будет задавать две строки,
# программа - определять количество вхождений одной строки в другой.

main_string = input('Type some text: ')
what_find = input('What we gonna find: ')
print(f'String "{what_find}" occurs {main_string.count(what_find)} times')
