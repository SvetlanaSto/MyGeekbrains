import pytest
from checker import checkout
import random, string
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def make_folders():
    return checkout("mkdir {} {} {} {}".format(data["folder_in"], data["folder_out"], data["folder_ext"],
                                               data["folder_ext2"]), "")


@pytest.fixture()
def clear_folders():
    return checkout("rm -rf {}/* {}/* {}/* {}/*".format(data["folder_in"], data["folder_out"], data["folder_ext"],
                                                        data["folder_ext2"]), "")


@pytest.fixture()
def make_files():
    list_of_files = []
    for i in range(data["count"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if checkout("cd {}; dd if=/dev/urandom of={} bs=1M count=1 iflag=fullblock".format(data["folder_in"],
                                                                                           filename), ""):
            list_of_files.append(filename)
    return list_of_files


@pytest.fixture()
def make_subfolder():
    testfilename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    if not checkout("cd {}; mkdir {}".format(data["folder_in"], subfoldername), ""):
        return None, None
    if not checkout(
            "cd {}/{}; dd if=/dev/urandom of={} bs={} count=1 iflag=fullblock".format(data["folder_in"], subfoldername,
                                                                                      testfilename, data["size"]), ""):
        return subfoldername, None
    else:
        return subfoldername, testfilename


@pytest.fixture(autouse=True)
def write_to_stat_txt():
    checkout("echo files count: {} >> stat.txt".format(data["count"]), "")
    checkout("echo file size: {} >> stat.txt".format(data["size"]), "")
    checkout("echo -n 'loadavg: ' >> stat.txt".format(data["size"]), "")
    checkout("cat /proc/loadavg >> stat.txt".format(data["size"]), "")
    return
