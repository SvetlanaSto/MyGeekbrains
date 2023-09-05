from zeep import Client, Settings
import logging
import yaml

with open("testdata.yaml") as f:
    data = yaml.safe_load(f)

wsdl = data["wsdl"]
settings = Settings(strict=False)
client = Client(wsdl=wsdl, settings=settings)


def check_text(text):
    response = client.service.checkText(text)
    logging.info(f'checkText response: {response}')

    return response[0]["s"]
