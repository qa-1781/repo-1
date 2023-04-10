import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


@pytest.mark.usefixtures("setup")
class test_search_and_verify_filters():
    def test_search_flights(self):




# Launching the Travel website
# Provide going from location
# Provide going to location
# Select the departure date
# Click on Flight search button

# Select the filter 1 stop
# Verify that the filtered result contains just 1 stop
