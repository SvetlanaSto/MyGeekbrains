def sort_by_lastname(file):
    lines = []

    with open(file, 'r', encoding="utf-8") as data:
        for line in data:
            lines.append(line)

    print(lines)
    sorted_lines = sorted(lines, key=lambda it: it.split(', ')[1])
    print(sorted_lines)

    with open(file, 'w', encoding="utf-8") as data:
        data.writelines(sorted_lines)

def sort_by_id(file):
    lines = []

    with open(file, 'r', encoding="utf-8") as data:
        for line in data:
            lines.append(line)

    print(lines)
    sorted_lines = sorted(lines, key=lambda it: it.split(', ')[0])
    print(sorted_lines)

    with open(file, 'w', encoding="utf-8") as data:
        data.writelines(sorted_lines)