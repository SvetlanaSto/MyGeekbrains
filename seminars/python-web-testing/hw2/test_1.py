import time

import yaml

from module import Site

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    site = Site(testdata['address'])


def test_step1(x_selector_1, x_selector_2, btn_selector, x_selector_3, expected_result_1):
    input1 = site.find_element('xpath', x_selector_1)
    input1.send_keys('test')
    input2 = site.find_element('xpath', x_selector_2)
    input2.send_keys('test')
    btn = site.find_element('css', btn_selector)
    btn.click()
    error_label = site.find_element('xpath', x_selector_3)
    result = error_label.text
    assert result == expected_result_1, 'test_failed'


def test_step2(x_selector_1, x_selector_2, btn_selector, x_selector_4, expected_result_2):
    input1 = site.find_element('xpath', x_selector_1)
    input1.clear()
    input1.send_keys(testdata['username'])

    input2 = site.find_element('xpath', x_selector_2)
    input2.clear()
    input2.send_keys(testdata['password'])

    btn = site.find_element('css', btn_selector)
    btn.click()

    link1 = site.find_element('xpath', x_selector_4)
    result = link1.text

    assert result == expected_result_2


def test_step3(btn_create_post, x_selector_5, x_selector_6, x_selector_7, btn_save_post, x_selector_8):
    btn = site.find_element('id', btn_create_post)
    btn.click()

    title = site.find_element('xpath', x_selector_5)
    title.clear()
    title.send_keys(testdata['title'])

    description = site.find_element('xpath', x_selector_6)
    description.clear()
    description.send_keys(testdata['description'])

    content = site.find_element('xpath', x_selector_7)
    content.clear()
    content.send_keys(testdata['content'])

    save_btn = site.find_element('xpath', btn_save_post)
    save_btn.click()

    time.sleep(testdata['sleep_time'])
    header = site.find_element('css', x_selector_8)
    result = header.text

    site.close()
    assert result == testdata['title']


