from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utilities.config_reader import ConfigReader


class DriverFactory:

    @staticmethod
    def get_driver():
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        if ConfigReader.should_maximize():
            driver.maximize_window()

        driver.implicitly_wait(ConfigReader.get_implicit_wait())

        return driver