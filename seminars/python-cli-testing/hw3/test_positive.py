from checker import checkout, getout
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)


def test_step1(make_folders, clear_folders, make_files):
    # test1
    res1 = checkout("cd {}; 7z a {}/arx -t{}".format(data["folder_in"], data["folder_out"], data["type"]),
                    "Everything is Ok")
    res2 = checkout("ls {}".format(data["folder_out"]), "arx.{}".format(data["type"]))
    assert res1 and res2, "test1 FAIL"


def test_step2(clear_folders, make_files):
    # test2
    res = []
    res.append(checkout("cd {}; 7z a {}/arx -t{}".format(data["folder_in"], data["folder_out"], data["type"]),
                        "Everything is Ok"))
    res.append(checkout("cd {}; 7z e arx.{} -o{} -y".format(data["folder_out"], data["type"], data["folder_ext"]),
                        "Everything is Ok"))
    for item in make_files:
        res.append(checkout("ls {}".format(data["folder_ext"]), item))
    assert all(res)


def test_step3():
    # test3
    assert checkout("cd {}; 7z t arx.{}".format(data["folder_out"], data["type"]), "Everything is Ok"), "test3 FAIL"


def test_step4():
    # test4
    assert checkout("cd {}; 7z u arx2.{}".format(data["folder_in"], data["type"]), "Everything is Ok"), "test4 FAIL"


def test_step5(clear_folders, make_files):
    # test5
    res = []
    res.append(checkout("cd {}; 7z a {}/arx -t{}".format(data["folder_in"], data["folder_out"], data["type"]),
                        "Everything is Ok"))
    for i in make_files:
        res.append(checkout("cd {}; 7z l arx.{}".format(data["folder_out"], data["type"]), i))
    assert all(res), "test5 FAIL"


def test_step6(clear_folders, make_files, make_subfolder):
    # test6
    res = []
    res.append(checkout("cd {}; 7z a {}/arx -t{}".format(data["folder_in"], data["folder_out"], data["type"]),
                        "Everything is Ok"))
    res.append(checkout("cd {}; 7z x arx.{} -o{} -y".format(data["folder_out"], data["type"], data["folder_ext2"]),
                        "Everything is Ok"))
    for i in make_files:
        res.append(checkout("ls {}".format(data["folder_ext2"]), i))
    res.append(checkout("ls {}".format(data["folder_ext2"]), make_subfolder[0]))
    res.append(checkout("ls {}/{}".format(data["folder_ext2"], make_subfolder[0]), make_subfolder[1]))
    assert all(res), "test6 FAIL"


def test_step7():
    # test7
    assert checkout("cd {}; 7z d arx.{}".format(data["folder_out"], data["type"]), "Everything is Ok"), "test7 FAIL"


def test_step8(clear_folders, make_files):
    # test8
    res = []
    for i in make_files:
        res.append(checkout("cd {}; 7z h {}".format(data["folder_in"], i), "Everything is Ok"))
        hash = getout("cd {}; crc32 {}".format(data["folder_in"], i)).upper()
        res.append(checkout("cd {}; 7z h {}".format(data["folder_in"], i), hash))
    assert all(res), "test8 FAIL"
