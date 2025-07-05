import time
import csv
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@allure.title("DemoQA Login Test with CSV Data")
@allure.description("""
This test:
- Opens DemoQA login page
- Reads user credentials from a CSV file
- Enters username and password
- Attempts login
- Repeats for all rows in CSV
""")
@allure.severity(allure.severity_level.CRITICAL)
def test_demoqa_login_from_csv():
    with allure.step("Setup Chrome WebDriver"):
        service = Service(r"C:\Users\HP\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe")  # ✅ Replace with your path
        options = Options()
        # options.add_argument("--headless=new")  # Uncomment to run headless
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()

    try:
        with allure.step("Open DemoQA login page"):
            driver.get("https://demoqa.com/login")
            wait = WebDriverWait(driver, 10)
            _attach_screenshot(driver, "Login Page Loaded")

        with allure.step("Read CSV file for login data"):
            with open('data.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    username = row['username']
                    password = row['password']

                    with allure.step(f"Login attempt for user: {username}"):
                        user_input = wait.until(EC.visibility_of_element_located((By.ID, "userName")))
                        driver.execute_script("arguments[0].scrollIntoView(true);", user_input)
                        ActionChains(driver).move_to_element(user_input).perform()
                        user_input.clear()
                        user_input.send_keys(username)

                        pass_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
                        driver.execute_script("arguments[0].scrollIntoView(true);", pass_input)
                        ActionChains(driver).move_to_element(pass_input).perform()
                        pass_input.clear()
                        pass_input.send_keys(password)

                        login_button = wait.until(EC.visibility_of_element_located((By.ID, "login")))
                        driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
                        login_button.click()

                        time.sleep(2)
                        _attach_screenshot(driver, f"After login attempt for {username}")

                        # Optionally, add assertion logic here:
                        # e.g. check for successful login indicator
                        # assert "profile" in driver.current_url.lower()

                        # Reset page for next login
                        driver.get("https://demoqa.com/login")

    finally:
        with allure.step("Close browser"):
            driver.quit()


def _attach_screenshot(driver, name):
    """Helper function to attach screenshots to Allure report."""
    screenshot = driver.get_screenshot_as_png()
    allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
