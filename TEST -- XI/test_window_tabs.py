import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@allure.title("Test Opening Multiple Browser Tabs")
@allure.description("""
This test:
- Opens Google
- Opens Wikipedia in a new tab
- Switches to Wikipedia tab and verifies the title
- Closes Wikipedia tab and returns to Google
""")
@allure.severity(allure.severity_level.CRITICAL)
def test_open_multiple_tabs():
    with allure.step("Setup Chrome WebDriver"):
        service = Service(r"C:\Users\HP\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe")
        options = Options()
        # Uncomment for headless mode if desired
        # options.add_argument("--headless=new")
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()

    try:
        with allure.step("Open Google homepage"):
            driver.get("https://www.google.com")
            time.sleep(2)
            _attach_screenshot(driver, "Google Homepage")

        with allure.step("Open Wikipedia in a new tab via JS"):
            driver.execute_script("window.open('https://www.wikipedia.org', '_blank');")
            time.sleep(2)

        with allure.step("Switch to Wikipedia tab and verify title"):
            tabs = driver.window_handles
            driver.switch_to.window(tabs[1])
            title = driver.title
            print("Title:", title)
            _attach_screenshot(driver, "Wikipedia Tab")
            assert "Wikipedia" in title

        with allure.step("Close Wikipedia tab and switch back to Google"):
            driver.close()
            driver.switch_to.window(tabs[0])
            _attach_screenshot(driver, "Returned to Google")

    finally:
        with allure.step("Quit the browser"):
            driver.quit()


def _attach_screenshot(driver, name):
    """Helper to attach screenshots in Allure."""
    screenshot = driver.get_screenshot_as_png()
    allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
