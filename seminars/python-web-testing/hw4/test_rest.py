import logging
import requests
import yaml

with open("testdata.yaml", encoding="utf-8") as f:
    testdata = yaml.safe_load(f)


def test_step1(rest_login):
    header = {"X-Auth-Token": rest_login}

    res = requests.get(testdata["address"] + "/api/posts",  # params={"owner": "notMe"},
                       headers=header)
    listres = [i["title"] for i in res.json()["data"]]
    logging.debug(f'Titles of posts: {listres}')

    assert testdata["test_title"] in listres, 'Test1 FAILED'


def test_step2(rest_login):
    header = {"X-Auth-Token": rest_login}

    requests.post(testdata["address"] + "/api/posts",
                  data={"title": testdata["test_title"],
                        "description": testdata["test_description"],
                        "content": testdata["test_content"]},
                  headers=header)

    res_get = requests.get(testdata["address"] + "/api/posts", headers=header)
    listres = [i["title"] for i in res_get.json()["data"]]
    logging.debug(f'Titles of posts after creating new post: {listres}')

    assert testdata["test_title"] in listres, 'Test2 FAILED'
