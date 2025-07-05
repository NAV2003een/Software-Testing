import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@allure.title("Login Test")
@allure.description("Test login functionality with valid credentials.")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_success():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")

    with allure.step("Enter username and password"):
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("Password123")

    with allure.step("Click Login button"):
        driver.find_element(By.ID, "submit").click()

    with allure.step("Validate login success"):
        success = driver.find_element(By.TAG_NAME, "h1").text
        assert "Logged In Successfully" in success

    driver.quit()
