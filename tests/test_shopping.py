import allure
import pytest

from pages.LandingPage import LandingPage
from utilities.Base import Base
from utilities.GetTestData import GetTestData


@allure.feature("shopping site")
class TestShopping(Base):
    @allure.story("user registration")
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_registration(self, get_data, setup):
        log = self.get_logger()
        landing_page = LandingPage(self.driver)
        with allure.step("Navigate to url and enter user details"):
            landing_page.enter_name(get_data["name"])
            landing_page.enter_email(get_data["email"])
            landing_page.enter_password(get_data["password"])
            landing_page.select_icecream_checkbox()
            landing_page.select_gender(get_data["gender"])
            landing_page.select_student()
            landing_page.enter_dob(get_data["dob"])
        with allure.step("Submit form"):
            landing_page.submit_form()
        with allure.step("Verify message displayed"):
            message = landing_page.get_alert_message()
            log.info("Alert displayed : " + message)
            try:
                assert "Success" in message, "Success is not in alert"
            except AssertionError as e:
                log.error(e)
                raise

    @allure.story("Shop product")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_e2e(self, get_e2e_data, setup):
        log = self.get_logger()
        product_needed = get_e2e_data["product_name"]
        landing_page = LandingPage(self.driver)
        with allure.step("Navigate to url and add product to cart"):
            products_page = landing_page.go_to_products()
            products_page.add_product_to_cart(product_needed)
        with allure.step("Navigate to cart and verify product name"):
            cart_page = products_page.go_to_cart()
            product_in_cart = cart_page.get_product_name()
            assert product_needed == product_in_cart
        with allure.step("checkout product"):
            confirmation_page = cart_page.checkout_product()
            country_needed = get_e2e_data["country"]
            confirmation_page.select_country(country_needed)
            confirmation_page.select_terms_checkbox()
            confirmation_page.purchase_order()
        with allure.step("verify confirmation alert"):
            message = confirmation_page.get_alert()
            log.info("Alert displayed : " + message)
            try:
                assert "Success!" in message
            except AssertionError as e:
                log.error(e)
                raise

    # data parameterization using tuple
    # @pytest.fixture(params=[("Dinu", "test@test.com", "tester@453", "Male", "11112012"),
    #                         ("Sini", "test@test.com", "testersini@453", "Female", "11112012")])
    # using dictionary
    # @pytest.fixture(params=[
    #     {"name": "Dinu", "email": "test@test.com", "password": "tester@453", "gender": "Male", "dob": "11112012"},
    #     {"name": "Sini", "email": "sini@test.com", "password": "tester@453", "gender": "Female", "dob": "11112012"}])
    # def get_data(self, request):
    #     return request.param

    @pytest.fixture(params=GetTestData.get_test_data("test_user_registration"))
    def get_data(self, request):
        return request.param

    @pytest.fixture(params=GetTestData.get_test_data("test_e2e"))
    def get_e2e_data(self, request):
        return request.param
