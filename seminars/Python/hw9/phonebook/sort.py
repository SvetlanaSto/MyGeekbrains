def sort_by_lastname(file):
    lines = []

    with open(file, 'r', encoding="utf-8") as data:
        for line in data:
            lines.append(line)

    sorted_lines = sorted(lines, key=lambda it: it.split(', ')[1])

    return ''.join(sorted_lines)

def sort_by_id(file):
    lines = []

    with open(file, 'r', encoding="utf-8") as data:
        for line in data:
            lines.append(line)

    sorted_lines = sorted(lines, key=lambda it: it.split(', ')[0])

    return ''.join(sorted_lines)
