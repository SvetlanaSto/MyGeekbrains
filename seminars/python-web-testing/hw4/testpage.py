import logging

import yaml
from selenium.webdriver.common.by import By

from BaseApp import BasePage


class TestSearchLocators:
    ids = dict()
    with open('locators.yaml', encoding="utf-8") as f:
        locators = yaml.safe_load(f)

    for locator in locators['xpath'].keys():
        ids[locator] = (By.XPATH, locators['xpath'][locator])

    for locator in locators['css'].keys():
        ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])


class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        """Method to enter text into a field given a locator and description"""
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send '{word}' to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operating with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        """Method to click a button given a locator and description"""
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception('Exception with click')
        logging.debug(f"Clicked {element_name}")

    def get_text_from_element(self, locator, description=None):
        """Retrieve text from an element"""
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while getting text from {element_name}')
            return None
        logging.debug(f'Found text {text} in field {element_name}')
        return text

    # ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'], word,
                                   description="Enter username in login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_PASS_FIELD'], word,
                                   description="Enter password in login form")

    def enter_post_title(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_POST_TITLE'], word,
                                   description="Enter title in post create form")

    def enter_post_description(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_POST_DESCRIPTION'], word,
                                   description="Enter description in post create form")

    def enter_post_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_POST_CONTENT'], word,
                                   description="Enter content in post create form")

    def enter_contact_us_name(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTACT_US_NAME_FIELD'], word,
                                   description="Enter name in contact us form")

    def enter_contact_us_email(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTACT_US_EMAIL_FIELD'], word,
                                   description="Enter email in contact us form")

    def enter_contact_us_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTACT_US_CONTENT_FIELD'], word,
                                   description="Enter content in contact us form")

    # CLICK BUTTON/LINK
    def click_login_button(self):
        logging.info("Click login button")
        self.click_button(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'], description='Login button')

    def click_create_post_btn(self):
        logging.info('Click create new post button')
        self.click_button(TestSearchLocators.ids['LOCATOR_CREATE_POST_BTN'], description='Create post button')

    def click_save_post_btn(self):
        logging.info('Click save post button')
        self.click_button(TestSearchLocators.ids['LOCATOR_SAVE_POST_BTN'], description='Save post button')

    def click_contact_us_btn(self):
        logging.info('Click contact us button')
        self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT_US_BTN'], description='Contact us button')

    def click_contact_link(self):
        logging.info("Click Contact Us")
        self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT_US_LINK'], description='Contact us link')

    # GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_ERROR_FIELD'],
                                          description='Get text after failed login')

    def get_login_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_HELLO_LOGIN'],
                                          description='Get text after successful login')

    def get_added_post_title(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_POST_ADDED'],
                                          description='Get title of created post')

    # OTHER OPERATIONS
    def get_alert(self):
        logging.info('Get alert text')
        text = self.get_alert_text()
        logging.info(text)
        return text
