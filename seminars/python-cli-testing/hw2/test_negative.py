from checker import checkout_negative

testdir = "/home/sveta/7ztest"
badarx = f"{testdir}/badarx"
folder = f"{testdir}/folder1"


def test_step1():
    # разархивируем архив arx2.7z в директорию folder1 и проверяем наличие файлов test1, test2 в директории folder1
    assert checkout_negative(cmd="cd {}; 7z e arx2.7z -o{} -y".format(badarx, folder), text="ERRORS"), "test1 FAIL"


def test_step2():
    # Мы проверяем целостность архива arx2.7z
    assert checkout_negative(cmd="cd {}; 7z t arx2.7z".format(badarx), text="ERRORS"), "test2 FAIL"
