# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

def find_duplicates(lst):
    element_counts = {}
    for element in lst:
        if element in element_counts:
            element_counts[element] += 1
        else:
            element_counts[element] = 1

    result = []
    for element, count in element_counts.items():
        if count > 1:
            result.append(element)

    return result


input_lst = [1, 2, 3, 4, 5, 6, 3, 2, 1, 4]
result_list = find_duplicates(input_lst)
print(result_list)
