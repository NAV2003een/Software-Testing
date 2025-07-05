import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@allure.title("JavaScript Alerts Handling Test")
@allure.description("""
Test handling of:
- Simple Alert
- Confirm Alert
- Prompt Alert
""")
@allure.severity(allure.severity_level.CRITICAL)
def test_javascript_alerts():
    with allure.step("Setup Chrome WebDriver"):
        service = Service(r"C:\Users\HP\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe")
        options = Options()
        # Uncomment below if you want headless:
        # options.add_argument("--headless=new")
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()

    try:
        with allure.step("Open Alerts Page"):
            driver.get("https://the-internet.herokuapp.com/javascript_alerts")
            time.sleep(1)
            _attach_screenshot(driver, "Loaded Alerts Page")

        # Simple Alert
        with allure.step("Handle Simple Alert"):
            driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
            time.sleep(1)
            alert = driver.switch_to.alert
            allure.attach(alert.text, name="Simple Alert Text", attachment_type=allure.attachment_type.TEXT)
            assert "I am a JS Alert" in alert.text
            alert.accept()
            _attach_screenshot(driver, "After Simple Alert")

        # Confirm Alert
        with allure.step("Handle Confirm Alert"):
            driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
            time.sleep(1)
            alert = driver.switch_to.alert
            allure.attach(alert.text, name="Confirm Alert Text", attachment_type=allure.attachment_type.TEXT)
            assert "I am a JS Confirm" in alert.text
            alert.dismiss()
            _attach_screenshot(driver, "After Confirm Alert")

        # Prompt Alert
        with allure.step("Handle Prompt Alert"):
            driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
            time.sleep(1)
            alert = driver.switch_to.alert
            allure.attach(alert.text, name="Prompt Alert Text", attachment_type=allure.attachment_type.TEXT)
            assert "I am a JS prompt" in alert.text
            alert.send_keys("Selenium Test")
            time.sleep(1)
            alert.accept()
            _attach_screenshot(driver, "After Prompt Alert")

        with allure.step("All alerts handled successfully"):
            result_text = driver.find_element(By.ID, "result").text
            allure.attach(result_text, name="Result Text", attachment_type=allure.attachment_type.TEXT)

    finally:
        with allure.step("Close Browser"):
            driver.quit()


def _attach_screenshot(driver, name):
    screenshot = driver.get_screenshot_as_png()
    allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
