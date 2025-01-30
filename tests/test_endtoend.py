# import time
#
# from pages.LandingPage import LandingPage
# from utilities.Base import Base
#
#
# class TestEndToEnd(Base):
#     def test_e2e(self):
#         product_needed = "Samsung Note 8"
#         landing_page = LandingPage(self.driver)
#         products_page = landing_page.go_to_products()
#         self.wait_for_elements_visible(products_page.product_cards)
#         product_cards = products_page.get_product_cards()
#         for product in product_cards:
#             if self.get_text(product.find_element(*products_page.product_title)) == product_needed:
#                 product.find_element(*products_page.add_to_cart_button).click()
#                 break
#         cart_page = products_page.go_to_cart()
#         self.wait_for_element_visible(cart_page.get_product_name())
#         product_in_cart = cart_page.get_product_name().text
#         assert product_needed == product_in_cart
#         confirmation_page = cart_page.checkout_product()
#         country_needed = "india"
#         self.wait_for_element_clickable(confirmation_page.get_country())
#         confirmation_page.get_country().send_keys(country_needed)
#         self.wait_for_elements_visible(confirmation_page.country_suggestions)
#         country_displayed = confirmation_page.get_country_suggestions()
#         for country in country_displayed:
#             if country.text.casefold() == country_needed.casefold():
#                 country.click()
#                 break
#         self.click_element(confirmation_page.get_terms_checkbox())
#         self.click_element(confirmation_page.get_submit_button())
#         message = self.get_text(confirmation_page.get_alert())
#         assert "Success!" in message
#
#     def test_form_submission(self):
#         landing_page = LandingPage(self.driver)
#         self.enter_text(landing_page.get_name(), "dinu")
#         self.enter_text(landing_page.get_email(), "dinu@test.com")
#         self.enter_text(landing_page.get_password(), "tester@435")
#         self.click_element(landing_page.get_icecream_checkbox())
#         self.select_dropdown_visible_text(landing_page.get_gender_dropdown(), "Female")
#         self.select_radio_option(landing_page.get_student_radio())
#         self.enter_text(landing_page.get_dob(), "11112012")
#         self.click_element(landing_page.get_submit_btn())
#         message = self.get_text(landing_page.get_success_alert())
#         assert "Success" in message
#
#
