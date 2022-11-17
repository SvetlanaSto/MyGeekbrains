def import_csv():
    result = []
    with open('import.csv', 'r') as file:
        for line in file:
            columns = line.strip().split(";")
            result.append((columns[0], columns[1], columns[2], columns[3]))
    return result