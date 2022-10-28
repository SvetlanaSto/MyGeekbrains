# Задача 4: Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data:
        return ''

    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding


def rle_decode(data):
    decode = ''
    count = ''

    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


f = open("task5_orig.txt", "r")
orig_data = f.read().rstrip()
f.close()
print("original data:", orig_data)

rle_encoded = rle_encode(orig_data)
print(f"encoded data: {rle_encoded}")

f = open('task5_rle.txt', 'w')
f.writelines(rle_encoded)
f.close()

rle_decoded = rle_decode(rle_encoded)
print(f"decoded data: {rle_decoded}")

print("decoded = original?", rle_decoded == orig_data)
