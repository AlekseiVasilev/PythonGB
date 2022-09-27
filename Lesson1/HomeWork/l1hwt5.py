# 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# in
# - 3 x1
# - 6 y1
# - 2 x2
# - 1 y2
# out
# 5.099

x1 = float(input("Enter value for X coordinate for 1-st point: "))
y1 = float(input("Enter value for Y coordinate for 1-st point: "))
x2 = float(input("Enter value for X coordinate for 2-nd point: "))
y2 = float(input("Enter value for Y coordinate for 2-nd point: "))
result = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f'Distance between first point [{x1}, {y1}] and second point [{x2}, {y2}] is: {result:.3f}')
