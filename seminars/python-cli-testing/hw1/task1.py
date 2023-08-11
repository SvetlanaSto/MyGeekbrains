# Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе
# и False в противном случае.
# Передаваться должна только одна строка, разбиение вывода использовать не нужно.


import subprocess


def has_substring_in_process_output(process: str, substr: str) -> bool:
    result = subprocess.run(process, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    out = result.stdout
    print(out)

    if result.returncode == 0:
        return substr in out
    else:
        return False


if __name__ == '__main__':
    has_substring = has_substring_in_process_output("cat /etc/os-release", 'VERSION="22.04.2 LTS (Jammy Jellyfish)"')
    print(f"{has_substring = }")
