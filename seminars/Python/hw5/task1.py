# Задача 1: Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

str = "аабвв ложд абвп прабв фыва сабв ааабв"
l = str.split()
print(l)
# решено с помощью list,filter,lambda
filtered = list(filter(lambda it: "абв" not in it, l))
print(' '.join(filtered))
