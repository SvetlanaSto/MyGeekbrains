import pytest
import yaml
import requests


with open("config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def correct_word():
    return "молоко"

@pytest.fixture()
def incorrect_word():
    return "малако"


@pytest.fixture()
def login():
    res = requests.post(data["address"] + "gateway/login",
                         data={"username": data["username"], "password": data["password"]})
    print(res.content)
    return res.json()["token"]


@pytest.fixture()
def testtext1():
    return "Заголовок 2"


@pytest.fixture()
def test2_title():
    return "test2 title"


@pytest.fixture()
def test2_description():
    return "test2 description"


@pytest.fixture()
def test2_content():
    return "test2 content"