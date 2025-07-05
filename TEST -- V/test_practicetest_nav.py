import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@allure.title("Practice Test Automation - Menu Navigation Test")
@allure.description("""
Test navigation of main menu items on https://practicetestautomation.com/
- Clicks 'Blog'
- Clicks 'Contact'
- Verifies correct redirection based on URL
""")
@allure.severity(allure.severity_level.CRITICAL)
def test_navigation_practicetest():

    with allure.step("Setup Chrome WebDriver"):
        # Replace with your chromedriver path
        service = Service(r"C:\Users\HP\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe")
        options = Options()
        # options.add_argument("--headless=new")  # remove comment to run headless
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()

    try:
        with allure.step("Open Practice Test Automation Homepage"):
            driver.get("https://practicetestautomation.com/")
            time.sleep(2)
            _attach_screenshot(driver, "Home Page")

        menu_items = {
            "Blog": ("a[href*='blog']", "blog"),
            "Contact": ("a[href*='contact']", "contact")
        }

        for name, (css_selector, expected_url_part) in menu_items.items():
            with allure.step(f"Click {name} link and verify redirection"):
                link = driver.find_element(By.CSS_SELECTOR, css_selector)
                link.click()
                time.sleep(2)

                current_url = driver.current_url
                allure.attach(
                    current_url,
                    name=f"URL after clicking {name}",
                    attachment_type=allure.attachment_type.TEXT
                )
                _attach_screenshot(driver, f"After clicking {name}")

                assert expected_url_part in current_url, f"Expected '{expected_url_part}' in URL, but got {current_url}"

                # Go back to homepage for next test
                driver.get("https://practicetestautomation.com/")
                time.sleep(2)

    finally:
        with allure.step("Close browser"):
            driver.quit()


def _attach_screenshot(driver, name):
    screenshot = driver.get_screenshot_as_png()
    allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
