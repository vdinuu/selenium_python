import pytest
from selenium import webdriver

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser name for execution"
    )


@pytest.fixture()
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
    yield
    driver.quit()
