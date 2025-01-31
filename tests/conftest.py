import os.path
import shutil

import allure
import pytest
from selenium import webdriver

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser name for execution"
    )


@pytest.fixture(scope="function")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name.lower() == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name.lower() == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--start-maximized')
        driver = webdriver.Firefox(options=firefox_options)
    elif browser_name.lower() == "edge":
        edge_options = webdriver.EdgeOptions()
        edge_options.add_argument('--start-maximized')
        driver = webdriver.Edge(options=edge_options)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def delete_allure_results():
    allure_results_dir = "./allure-results"
    if os.path.exists(allure_results_dir):
        shutil.rmtree(allure_results_dir)
    os.makedirs(allure_results_dir, exist_ok=True)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture screenshot on test failure.
    """
    outcome = yield
    report = outcome.get_result()

    # Check if the test failed
    if report.when == "call" and report.failed:
        # Check if the test has a 'driver' fixture (Selenium WebDriver)
        driver_fixture = item.funcargs.get("setup")
        if driver_fixture is not None:
            screenshot_path = "allure-results/screenshot.png"
            # Take a screenshot
            driver_fixture.save_screenshot(screenshot_path)
            # Attach the screenshot to the Allure report
            allure.attach.file(
                screenshot_path,
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
