import delete
import write
import print1
import edit
import search
import sort

while True:
    print("База данных сотрудников.\n")
    print('1. Вывести все записи.\n2. Добавить запись.\n3. Найти запись.\n4. Изменить запись.\n' +
    '5. Удалить запись.\n6. Отсортировать по фамилии.\n7. Отсортировать по id.\n8. Выход.\n')

    value = int(input("Выберите действие: "))
    print(value)
    if value == 1:
        print1.print_all_to_console()
    elif value == 2:
        write.new_entry()
    elif value == 3:
        search.search_entry('employees.csv')
    elif value == 4:
        edit.edit_entry('employees.csv')
    elif value == 5:
        delete.delete_entry('employees.csv')
    elif value == 6:
        sort.sort_by_lastname('employees.csv')
    elif value == 7:
        sort.sort_by_id('employees.csv')
    elif value == 8:
        break
