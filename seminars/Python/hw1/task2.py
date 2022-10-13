# 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in True, False:
    for y in True, False:
        for z in True, False:
            left_side = not (x or y or z)
            right_side = not x and not y and not z
            print(f'x={x}, y={y}, z={z}: слева {left_side}, справа {right_side}')
