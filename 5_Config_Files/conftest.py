import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="class")                    ### Setup
def setup(request):

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.booking.com/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    request.cls.driver = driver
    request.cls.wait = wait

    yield

    driver.close()           ### teardown