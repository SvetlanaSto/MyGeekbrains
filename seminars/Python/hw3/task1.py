# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

numbers = list(range(1, 10))
print(numbers)

sum = 0
for i in range(1, len(numbers)-1, 2):
    sum += numbers[i]

print(f'Сумма элементов на нечетных позициях равна: {sum}')
