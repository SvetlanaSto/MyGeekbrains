# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
quadrant = int(input('Введите номер четверти: '))

if quadrant == 1: 
    print('x > 0 and y > 0')
elif quadrant == 2:
    print('x < 0 and y > 0')
elif quadrant == 3:
    print('x < 0 and y < 0')
elif quadrant == 4:
    print('x > 0 and y < 0')
else:
    print('Некорректный ввод данных')
