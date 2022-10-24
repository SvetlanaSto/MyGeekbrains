#Задача 5: Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

first = []
with open("file.txt", "r") as file:
    for line in file:
        first.append(int(line))
print("first:", first)

second = []
with open("file2.txt", "r") as file:
    for line in file:
        second.append(int(line))
print("second:", second)

diff = len(first) - len(second)

if (diff > 0):
    for i in range(diff):
        second.insert(0, 0)
elif (diff < 0):
    for i in range(-diff):
        first.insert(0, 0)

result = []
for i in range(len(first)):
    result.append(first[i] + second[i])

print("result:", result)

f = open('task5_result.txt', 'w')
for i in result:
    f.write(str(i) + "\n")
f.close()