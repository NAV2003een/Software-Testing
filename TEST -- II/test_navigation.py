import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@allure.title("Browser Navigation Test")
@allure.description("""
This test:
- Opens Google
- Navigates to Wikipedia
- Goes back
- Goes forward
- Refreshes the page
- Prints current URL
""")
@allure.severity(allure.severity_level.CRITICAL)
def test_navigation():

    with allure.step("Setup Chrome WebDriver"):
        # ✅ Replace this path with YOUR chromedriver.exe path if needed
        service = Service(r"C:\Users\HP\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe")
        options = Options()
        options.add_argument("--headless=new")  # Remove this line if you want to see the browser
        driver = webdriver.Chrome(service=service, options=options)

    try:
        with allure.step("Open Google homepage"):
            driver.maximize_window()
            driver.get("https://www.google.com")
            allure.attach(driver.title, name="Google Title", attachment_type=allure.attachment_type.TEXT)
            allure.attach(driver.current_url, name="Google URL", attachment_type=allure.attachment_type.TEXT)
            _attach_screenshot(driver, "Google Homepage")
            time.sleep(2)

        with allure.step("Navigate to Wikipedia"):
            driver.get("https://www.wikipedia.org")
            allure.attach(driver.title, name="Wikipedia Title", attachment_type=allure.attachment_type.TEXT)
            allure.attach(driver.current_url, name="Wikipedia URL", attachment_type=allure.attachment_type.TEXT)
            _attach_screenshot(driver, "Wikipedia Homepage")
            time.sleep(2)

        with allure.step("Go Back to Google"):
            driver.back()
            allure.attach(driver.title, name="Back Page Title", attachment_type=allure.attachment_type.TEXT)
            allure.attach(driver.current_url, name="Back Page URL", attachment_type=allure.attachment_type.TEXT)
            _attach_screenshot(driver, "After Back Navigation")
            time.sleep(2)

        with allure.step("Go Forward to Wikipedia"):
            driver.forward()
            allure.attach(driver.title, name="Forward Page Title", attachment_type=allure.attachment_type.TEXT)
            allure.attach(driver.current_url, name="Forward Page URL", attachment_type=allure.attachment_type.TEXT)
            _attach_screenshot(driver, "After Forward Navigation")
            time.sleep(2)

        with allure.step("Refresh the page"):
            driver.refresh()
            allure.attach(driver.title, name="Refreshed Page Title", attachment_type=allure.attachment_type.TEXT)
            allure.attach(driver.current_url, name="Refreshed Page URL", attachment_type=allure.attachment_type.TEXT)
            _attach_screenshot(driver, "After Refresh")
            time.sleep(2)

        with allure.step("Print final URL"):
            print("Current URL:", driver.current_url)

    finally:
        with allure.step("Close browser"):
            driver.quit()


def _attach_screenshot(driver, name):
    screenshot = driver.get_screenshot_as_png()
    allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)

