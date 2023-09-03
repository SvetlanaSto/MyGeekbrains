import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os, platform

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    browser_type = testdata['browser']


@pytest.fixture(scope='session')
def browser():
    if browser_type == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        if platform.system() == 'Linux' and os.path.exists("/snap/firefox"):
            options.binary_location = "/snap/firefox/current/usr/lib/firefox/firefox"
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    # driver.implicitly_wait(testdata['implicitly_wait'])
    # driver.maximize_window()
    yield driver
    driver.quit()
