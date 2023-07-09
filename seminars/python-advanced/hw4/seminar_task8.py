# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s
# (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.


def replace_variables():
    globals_dict = globals()
    new_vars = {}
    for var_name, var_value in globals_dict.items():
        if var_name.endswith('s') and len(var_name) > 1:
            new_var_name = var_name[:-1]
            new_vars[new_var_name] = var_value
            globals_dict[var_name] = None
    globals_dict.update(new_vars)


if __name__ == '__main__':
    a = 10
    b = '20s'
    c = 'Hello'
    cs = 'Hellos'
    ds = [1, 2, 3]
    s = 'S'

    print('before:')
    print('a:', a)  # 10
    print('b:', b)  # 20s
    print('c:', c)  # Hello
    print('cs:', cs)  # Hellos
    print('ds:', ds)  # [1, 2, 3]
    print('s:', s)  # S

    replace_variables()

    print('after:')
    print('a:', a)  # 10
    print('b:', b)  # 20s
    print('c:', c)  # Hellos
    print('cs:', cs)  # None
    print('d:', d)  # [1, 2, 3]
    print('ds:', ds)  # None
    print('s:', s)  # S
