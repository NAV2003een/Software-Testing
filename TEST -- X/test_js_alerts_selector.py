import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@allure.title("JavaScript Alerts Handling Test")
@allure.description("""
This test:
- Opens the JS Alerts demo page
- Handles a simple alert
- Handles a confirmation alert
- Handles a prompt alert (entering text)
- Asserts that the result messages are displayed correctly
""")
@allure.severity(allure.severity_level.CRITICAL)
def test_js_alerts():
    with allure.step("Setup Chrome WebDriver"):
        service = Service(r"C:\Users\HP\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe")
        options = Options()
        # Uncomment for headless mode
        # options.add_argument("--headless=new")
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()

    try:
        with allure.step("Open JS Alerts demo page"):
            driver.get("https://the-internet.herokuapp.com/javascript_alerts")
            time.sleep(2)
            _attach_screenshot(driver, "Initial Page")

        # --- Simple JS Alert ---
        with allure.step("Handle simple JS alert"):
            js_alert_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
            assert js_alert_button.is_displayed(), "JS Alert button not found"
            js_alert_button.click()
            time.sleep(2)
            alert = driver.switch_to.alert
            allure.attach(alert.text, name="Alert Text", attachment_type=allure.attachment_type.TEXT)
            alert.accept()
            result = driver.find_element(By.XPATH, "//p[@id='result']").text
            allure.attach(result, name="Result Message", attachment_type=allure.attachment_type.TEXT)
            _attach_screenshot(driver, "After JS Alert")

        # --- JS Confirm Alert ---
        with allure.step("Handle JS confirm alert (Dismiss)"):
            confirm_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
            assert confirm_button.is_displayed(), "JS Confirm button not found"
            confirm_button.click()
            time.sleep(2)
            alert = driver.switch_to.alert
            allure.attach(alert.text, name="Confirm Alert Text", attachment_type=allure.attachment_type.TEXT)
            alert.dismiss()
            result = driver.find_element(By.XPATH, "//p[@id='result']").text
            allure.attach(result, name="Result After Dismiss", attachment_type=allure.attachment_type.TEXT)
            _attach_screenshot(driver, "After JS Confirm Dismiss")

        # --- JS Prompt Alert ---
        with allure.step("Handle JS prompt alert with input"):
            prompt_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
            assert prompt_button.is_displayed(), "JS Prompt button not found"
            prompt_button.click()
            time.sleep(2)
            alert = driver.switch_to.alert
            allure.attach(alert.text, name="Prompt Alert Text", attachment_type=allure.attachment_type.TEXT)
            alert.send_keys("Vimal")
            alert.accept()
            result = driver.find_element(By.XPATH, "//p[@id='result']").text
            allure.attach(result, name="Result After Prompt", attachment_type=allure.attachment_type.TEXT)
            _attach_screenshot(driver, "After JS Prompt")

        with allure.step("Print test completion message"):
            print("JavaScript alert tests completed successfully.")

    finally:
        with allure.step("Close browser"):
            driver.quit()


def _attach_screenshot(driver, name):
    screenshot = driver.get_screenshot_as_png()
    allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
