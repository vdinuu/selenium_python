from selenium.webdriver.common.by import By

from pages.ProductsPage import ProductsPage
from utilities.Base import Base


class LandingPage(Base):
    def __init__(self, driver):
        self.driver = driver
        self.shop_link = (By.XPATH, "//a[contains(@href, '/shop')]")
        self.name_textbox = (By.CSS_SELECTOR, ".form-group input[name='name']")
        self.email_textbox = (By.CSS_SELECTOR, ".form-group input[name='email']")
        self.password_textbox = (By.CSS_SELECTOR, ".form-group input[placeholder='Password']")
        self.icecream_checkbox = (By.ID, "exampleCheck1")
        self.gender_dropdown = (By.ID, "exampleFormControlSelect1")
        self.student_radio = (By.ID, "inlineRadio1")
        self.employee_radio = (By.ID, "inlineRadio2")
        self.radio_options = (By.CSS_SELECTOR, "input[name='inlineRadioOptions']")
        self.dob = (By.CSS_SELECTOR, "input[name='bday']")
        self.submit_button = (By.CSS_SELECTOR, "input.btn-success")
        self.success_alert = (By.CSS_SELECTOR, "div.alert-success")

    def enter_name(self, text_to_enter):
        self.enter_text(self.name_textbox, text_to_enter)

    def enter_email(self, email):
        self.enter_text(self.email_textbox, email)

    def enter_password(self, password):
        self.enter_text(self.password_textbox, password)

    def select_icecream_checkbox(self):
        self.click_element(self.icecream_checkbox)

    def select_gender(self, dropdown_text):
        self.select_dropdown_visible_text(self.gender_dropdown, dropdown_text)

    def select_student(self):
        self.select_radio_option(self.student_radio)

    def enter_dob(self, dob):
        self.enter_text(self.dob, dob)

    def get_alert_message(self):
        return self.get_text(self.success_alert)

    def submit_form(self):
        self.click_element(self.submit_button)

    def go_to_products(self):
        self.click_element(self.shop_link)
        return ProductsPage(self.driver)
