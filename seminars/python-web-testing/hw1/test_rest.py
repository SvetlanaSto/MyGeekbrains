import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_step1(login, testtext1):
    header = {"X-Auth-Token": login}

    res = requests.get(data["address"] + "api/posts", #params={"owner": "notMe"},
                       headers=header)
    listres = [i["title"] for i in res.json()["data"]]
    #print(listres)

    assert testtext1 in listres, 'Test1 FAILED'
    
    
def test_step2(login, test2_title, test2_description, test2_content):
    header = {"X-Auth-Token": login}

    requests.post(data["address"] + "api/posts",
                         data={"title": test2_title, "description": test2_description, "content": test2_content},
                         headers=header)
                         
    resGet = requests.get(data["address"] + "api/posts", headers=header)
    listres = [i["title"] for i in resGet.json()["data"]]
    
    assert test2_title in listres, 'Test2 FAILED'
