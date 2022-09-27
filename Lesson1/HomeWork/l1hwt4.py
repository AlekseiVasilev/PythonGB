# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Type quarter number: '))
if quarter > 4 or quarter < 1:
    print(f'Quarter {quarter} is not exist')
elif quarter == 1:
    print(f'Coordinate range: x > 0, y > 0')
elif quarter == 2:
    print(f'Coordinate range: x < 0, y > 0')
elif quarter == 3:
    print(f'Coordinate range: x < 0, y < 0')
else:
    print(f'Coordinate range: x > 0, y < 0')
