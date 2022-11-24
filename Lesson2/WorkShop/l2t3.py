# 3. Напишите программу, в которой пользователь будет задавать две строки,
# программа - определять количество вхождений одной строки в другой.

# main_string = input('Type some text: ')
# what_find = input('What we gonna find: ')
# print(f'String "{what_find}" occurs {main_string.count(what_find)} times')

a = list(input())
b = list(input())
cnt = 0
for i in range(len(a)):
    if a[i] == b[0]:
        for j in range(len(b)):
            if a[i+j] != b[j]:
                break
        cnt += 1
print(cnt)
