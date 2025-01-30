from selenium.webdriver.common.by import By

from utilities.Base import Base


class ConfirmationPage(Base):
    def __init__(self, driver):
        self.driver = driver
        self.country = (By.ID, "country")
        self.country_suggestions = (By.CSS_SELECTOR, "div.suggestions li a")
        self.terms_checkbox = (By.CSS_SELECTOR, "div.checkbox-primary")
        self.purchase_button = (By.CSS_SELECTOR, "input[type='submit']")
        self.alert = (By.CSS_SELECTOR, "div.alert")

    def select_country(self, country_name):
        self.enter_text(self.country, country_name[0:3])
        self.wait_for_elements_visible(self.country_suggestions)
        for country in self.find_elements(self.country_suggestions):
            if self.get_text_element(country).casefold() == country_name.casefold():
                self.click_web_element(country)
                break

    def select_terms_checkbox(self):
        return self.click_element(self.terms_checkbox)

    def purchase_order(self):
        return self.click_element(self.purchase_button)

    def get_alert(self):
        return self.get_text(self.alert)