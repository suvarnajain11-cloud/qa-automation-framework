from utilities.driver_factory import DriverFactory


def test_launch_browser():
    driver = DriverFactory.get_driver()
    driver.get("https://www.saucedemo.com")
    print(driver.title)
    driver.quit()