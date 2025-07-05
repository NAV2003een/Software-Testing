import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@allure.title("Open Google Homepage")
@allure.description("This test launches Chrome, opens Google.com, and verifies the page title.")
@allure.severity(allure.severity_level.CRITICAL)
def test_open_google():

    with allure.step("Setup Chrome WebDriver"):
        service = Service(r"C:\Users\HP\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe")
        options = Options()
        options.add_argument("--headless=new")  # Optional: run headless
        driver = webdriver.Chrome(service=service, options=options)

    try:
        with allure.step("Navigate to Google.com"):
            driver.get("https://www.google.com/")

        with allure.step("Take screenshot of the page"):
            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name="Google_Homepage",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Verify page title contains 'Google'"):
            assert "Google" in driver.title

        with allure.step("Log success message"):
            print("Successfully opened Google.com")

    finally:
        with allure.step("Close browser"):
            driver.quit()
