import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@allure.title("Google Search Test for 'Amazon'")
@allure.description("""
This test:
- Opens Google homepage
- Searches for "Amazon"
- Submits the search
- Verifies page title
""")
@allure.severity(allure.severity_level.CRITICAL)
def test_google_search_amazon():
    with allure.step("Setup Chrome WebDriver"):
        service = Service(r"C:\Users\HP\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe")  # ✅ Replace with your path
        options = Options()
        # options.add_argument("--headless=new")  # Optional: run in headless mode
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()

    try:
        with allure.step("Open Google homepage"):
            driver.get("https://www.google.com/")
            time.sleep(2)
            _attach_screenshot(driver, "Google Homepage")

        with allure.step("Enter search query 'Amazon'"):
            search_box = driver.find_element(By.NAME, "q")
            search_box.send_keys("Amazon")
            _attach_screenshot(driver, "Entered 'Amazon' in search box")

        with allure.step("Submit the search"):
            search_box.send_keys(Keys.RETURN)
            time.sleep(3)
            _attach_screenshot(driver, "Search Results")

        with allure.step("Verify title contains 'Amazon'"):
            assert "Amazon" in driver.title

    finally:
        with allure.step("Close browser"):
            driver.quit()


def _attach_screenshot(driver, name):
    """Helper to attach screenshots to Allure."""
    screenshot = driver.get_screenshot_as_png()
    allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
