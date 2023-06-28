def print_line(first_num, columns, row_num):
    for i in range(first_num, columns + first_num):
        print(f"{i} X {row_num} = {i * row_num}", end='\t\t')
    print()


print('                     ТАБЛИЦА УМНОЖЕНИЯ')

for j in range(2, 11):
    print_line(2, 4, j)

print()

for j in range(2, 11):
    print_line(6, 4, j)
