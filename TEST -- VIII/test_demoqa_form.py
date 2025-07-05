import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@allure.title("DemoQA Practice Form Automation Test")
@allure.description("""
This test:
- Opens https://demoqa.com/automation-practice-form
- Fills out form fields: first name, last name, email, number, DOB
- Selects Male gender
- Takes screenshots at key points
""")
@allure.severity(allure.severity_level.CRITICAL)
def test_demoqa_form():
    with allure.step("Setup Chrome WebDriver"):
        service = Service(r"C:\Users\HP\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe")
        options = Options()
        # Uncomment for headless mode:
        # options.add_argument("--headless=new")
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()

    try:
        with allure.step("Open DemoQA Automation Practice Form"):
            driver.get("https://demoqa.com/automation-practice-form")
            time.sleep(2)
            _attach_screenshot(driver, "Opened Practice Form")

        with allure.step("Enter first name"):
            first_name = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
            assert first_name.is_displayed(), "First name field not found"
            first_name.send_keys("Vimal")
            time.sleep(1)

        with allure.step("Enter last name"):
            last_name = driver.find_element(By.XPATH, "(//input[@type='text'])[2]")
            assert last_name.is_displayed(), "Last name field not found"
            last_name.send_keys("raj")
            time.sleep(1)

        with allure.step("Enter email"):
            email = driver.find_element(By.XPATH, "(//input[@type='text'])[3]")
            assert email.is_displayed(), "Email field not found"
            email.send_keys("sjfniouef@fowi.com")
            time.sleep(1)

        with allure.step("Enter mobile number"):
            number = driver.find_element(By.XPATH, "(//input[@type='text'])[4]")
            assert number.is_displayed(), "Mobile number field not found"
            number.send_keys("6494987")
            time.sleep(1)

        with allure.step("Enter date of birth"):
            dob = driver.find_element(By.XPATH, "(//input[@type='text'])[5]")
            assert dob.is_displayed(), "DOB field not found"
            dob.clear()
            dob.send_keys("27 Nov 2004")
            time.sleep(1)

        with allure.step("Select gender: Male"):
            male_label = driver.find_element(By.XPATH, "//label[text()='Male']")
            assert male_label.is_displayed(), "Male gender option not found"
            male_label.click()
            time.sleep(1)

        with allure.step("Verify form partially filled"):
            _attach_screenshot(driver, "Form Partially Filled")

    finally:
        with allure.step("Close browser"):
            driver.quit()


def _attach_screenshot(driver, name):
    screenshot = driver.get_screenshot_as_png()
    allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
