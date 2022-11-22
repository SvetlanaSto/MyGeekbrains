def new_entry():
    ID = input('Введите ID: ')
    lastname = input('Введите фамилию: ')
    firstname = input('Введите имя: ')
    father_name = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')
    department = input('Введите отдел: ')
    position = input('Введите должность: ')
    with open('employees.csv','a', encoding='utf-8') as book:
        book.write(f'{ID}, {lastname}, {firstname}, {father_name}, {phone}, {department}, {position};\n')