from checker import checkout_negative
import yaml


with open('config.yaml') as f:
    data = yaml.safe_load(f)


def test_step1():
    # разархивируем архив arx2.7z в директорию folder1 и проверяем наличие файлов test1, test2 в директории folder1
    assert checkout_negative(cmd="cd {}; 7z e arx2.7z -o{} -y".format(data["badarx"], data["folder_ext"]), text="ERRORS"), "test1 FAIL"


def test_step2():
    # Мы проверяем целостность архива arx2.7z
    assert checkout_negative(cmd="cd {}; 7z t arx2.7z".format(data["badarx"]), text="ERRORS"), "test2 FAIL"
