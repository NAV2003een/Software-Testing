import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@allure.title("Techlistic Selenium Practice Form Automation")
@allure.description("""
This test:
- Opens https://www.techlistic.com/p/selenium-practice-form.html
- Fills in first name and last name fields
- Takes screenshots at each step
""")
@allure.severity(allure.severity_level.CRITICAL)
def test_techlistic_form():
    with allure.step("Setup Chrome WebDriver"):
        service = Service(r"C:\Users\HP\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe")
        options = Options()
        # Uncomment for headless:
        # options.add_argument("--headless=new")
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()

    try:
        with allure.step("Open Techlistic Practice Form page"):
            driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
            time.sleep(2)
            _attach_screenshot(driver, "Opened Techlistic Form")

        with allure.step("Fill in first name"):
            first_name = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
            assert first_name.is_displayed(), "First name field not found"
            first_name.clear()
            first_name.send_keys("Mahesh")
            time.sleep(1)
            _attach_screenshot(driver, "First Name Filled")

        with allure.step("Fill in last name"):
            last_name = driver.find_element(By.XPATH, "(//input[@type='text'])[2]")
            assert last_name.is_displayed(), "Last name field not found"
            last_name.clear()
            last_name.send_keys("Varan")
            time.sleep(1)
            _attach_screenshot(driver, "Last Name Filled")

        with allure.step("Log completion message"):
            print("Form filled successfully.")
            allure.attach("All alerts handled.", name="Log", attachment_type=allure.attachment_type.TEXT)

    finally:
        with allure.step("Close browser"):
            driver.quit()


def _attach_screenshot(driver, name):
    screenshot = driver.get_screenshot_as_png()
    allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
