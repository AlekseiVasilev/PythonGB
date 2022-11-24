# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = float(input('Enter value of X coordinate: '))
y = float(input('Enter value of Y coordinate: '))
if x > 0 and y > 0:
    print(f'Point [{x}, {y}] in 1-st quarter')
elif x > 0 and y < 0:
    print(f'Point [{x}, {y}] in 4-th quarter')
elif x < 0 and y > 0:
    print(f'Point [{x}, {y}] in 2-nd quarter')
elif x < 0 and y < 0:
    print(f'Point [{x}, {y}] in 3-rd quarter')
else:
    print(f'Values is incorrect. Point is on axis')
