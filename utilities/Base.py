import inspect
import logging
import os

import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.usefixtures("setup")
class Base:

    def get_logger(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(script_dir, ".."))
        log_dir = os.path.join(project_root, "logs")
        os.makedirs(log_dir, exist_ok=True)
        log_file_path = os.path.join(log_dir, "logfile.log")
        print(log_file_path)
        logger_name = inspect.stack()[1][3]
        log = logging.getLogger(logger_name)
        filehandler = logging.FileHandler(log_file_path, mode='w')
        log_format = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(log_format)
        log.addHandler(filehandler)
        log.setLevel(logging.INFO)
        return log

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def wait_for_element_visible(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(ec.visibility_of(self.find_element(locator)))

    def wait_for_elements_visible(self, elements_locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(ec.visibility_of_all_elements_located(elements_locator))

    def wait_for_element_clickable(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(ec.element_to_be_clickable(self.find_element(locator)))

    def click_element(self, locator):
        self.wait_for_element_clickable(locator)
        self.find_element(locator).click()

    def get_text(self, locator):
        self.wait_for_element_visible(locator)
        return self.find_element(locator).text

    def enter_text(self, locator, text_to_enter):
        self.wait_for_element_visible(locator)
        self.find_element(locator).send_keys(text_to_enter)

    def select_dropdown_visible_text(self, locator, text_to_select):
        select = Select(self.driver.find_element(*locator))
        select.select_by_visible_text(text_to_select)

    def select_radio_option(self, locator):
        element = self.find_element(locator)
        if not element.is_selected():
            self.click_element(locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def find_child_element(self, element, locator):
        return element.find_element(*locator)

    def get_text_child(self, element, locator):
        return self.find_child_element(element, locator).text

    def click_child_element(self, element, locator):
        self.find_child_element(element, locator).click()

    def wait_for_web_element_visible(self, element, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(ec.visibility_of(element))

    def wait_for_web_element_clickable(self, element, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(ec.element_to_be_clickable(element))

    def get_text_element(self, element):
        self.wait_for_web_element_visible(element)
        return element.text

    def click_web_element(self, element):
        self.wait_for_web_element_clickable(element)
        element.click()

