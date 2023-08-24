from sshcheckers import ssh_checkout_negative

import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)


class Testneg:
    def test_step1(self, make_folders, make_bad_arx):
        assert ssh_checkout_negative(data["host"], data["user"], data["passwd"],
                                     "cd {}; 7z e {}.{} -o{} -y".format(data["folder_out"], make_bad_arx, data["type"],
                                                                        data["folder_ext"]), "ERROR:"), "test1 FAIL"

    def test_step2(self, make_bad_arx):
        assert ssh_checkout_negative(data["host"], data["user"], data["passwd"],
                                     "cd {}; 7z t {}.{}".format(data["folder_out"], make_bad_arx,
                                                                data["type"]), "ERROR:"), "test2 FAIL"
