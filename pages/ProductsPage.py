from selenium.webdriver.common.by import By

from pages.CartPage import CartPage
from utilities.Base import Base


class ProductsPage(Base):
    def __init__(self, driver):
        self.driver = driver
        self.product_cards = (By.CSS_SELECTOR, "app-card div.card")
        self.product_title = (By.CSS_SELECTOR, "h4.card-title")
        self.checkout_button = (By.XPATH, "//a[contains(text(), 'Checkout')]")
        self.add_to_cart_button = (By.CSS_SELECTOR, "div button")

    def get_product_cards(self):
        return self.find_elements(self.product_cards)

    def go_to_cart(self):
        self.click_element(self.checkout_button)
        return CartPage(self.driver)

    def add_product_to_cart(self, product_name):
        self.wait_for_elements_visible(self.product_cards)
        for product in self.get_product_cards():
            if self.get_text_child(product, self.product_title) == product_name:
                self.click_child_element(product, self.add_to_cart_button)
                break
