from checker import checkout

testdir = "/home/sveta/7ztest"
tst = f"{testdir}/tst"
out = f"{testdir}/out"
folder = f"{testdir}/folder1"
folder2 = f"{testdir}/folder2"


def test_step1():
    # создаем архив arx2 и проверяем его наличие в директории out
    res1 = checkout(cmd="cd {}; 7z a {}/arx2".format(tst, out), text="Everything is Ok")
    res2 = checkout(cmd="ls {}".format(out), text="arx2.7z")
    assert res1 and res2, "test1 FAIL"


def test_step2():
    # разархивируем архив arx2.7z через e в директорию folder1 и проверяем наличие файлов test1, test2
    resl = checkout(cmd="cd {}; 7z e arx2.7z -o{} -y".format(out, folder), text="Everything is Ok")
    res2 = checkout(cmd="ls {}".format(folder), text="test1")
    res3 = checkout(cmd="ls {}".format(folder), text="test2")

    assert resl and res2 and res3, "test2 FAIL"


def test_step3():
    # разархивируем архив arx2.7z через x в директорию folder2 и проверяем наличие файлов test1, test2
    res1 = checkout(cmd="cd {}; 7z x arx2.7z -o{} -y".format(out, folder2), text="Everything is Ok")
    res2 = checkout(cmd="ls {}".format(folder2), text="test1")
    res3 = checkout(cmd="ls {}".format(folder2), text="test2")

    assert res1 and res2 and res3, "test3 FAIL"


def test_step4():
    # Проверяем список файлов архива arx2.7z
    assert checkout(cmd="cd {}; 7z l arx2.7z".format(out), text="2 files"), "test4 FAIL"


def test_step5():
    # Мы проверяем целостность архива arx2.7z
    assert checkout(cmd="cd {}; 7z t arx2.7z".format(out), text="Everything is Ok"), "test5 FAIL"


def test_step6():
    # Проверяем возможность обновить файлы в архиве arx2.7z
    assert checkout(cmd="cd {}; 7z u {}/arx2.7z".format(tst, out), text="Everything is Ok"), "test6 FAIL"


def test_step7():
    # Удаляем файлы из архива
    assert checkout(cmd="cd {}; 7z d arx2.7z".format(out), text="Everything is Ok"), "test7 FAIL"


def test_step8():
    # Проверяем хеш-сумму
    res1 = checkout(cmd="cd {}; 7z h arx2.7z".format(out), text="104DFD7B")
    res2 = checkout(cmd="cd {}; crc32 arx2.7z".format(out), text="104dfd7b")
    assert res1 and res2, "test7 FAIL"
