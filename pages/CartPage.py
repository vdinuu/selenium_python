from selenium.webdriver.common.by import By

from pages.ConfirmationPage import ConfirmationPage
from utilities.Base import Base


class CartPage(Base):
    def __init__(self, driver):
        self.driver = driver
        self.product_name = (By.CSS_SELECTOR, "h4.media-heading a")
        self.checkout_button = (By.CSS_SELECTOR, "button.btn-success")

    def get_product_name(self):
        return self.get_text(self.product_name)

    def checkout_product(self):
        self.click_element(self.checkout_button)
        return ConfirmationPage(self.driver)