from utilities.config_reader import ConfigReader


def test_launch_browser(driver):
    driver.get(ConfigReader.get_base_url())
    print(driver.title)