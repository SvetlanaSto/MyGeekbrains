import yaml

from soap_check_text import check_text

with open("testdata.yaml", encoding="utf-8") as f:
    testdata = yaml.safe_load(f)


def test_step1():
    assert testdata["test_soap_correct_word"] in check_text(testdata["test_soap_incorrect_word"]), 'Test1 FAILED'
