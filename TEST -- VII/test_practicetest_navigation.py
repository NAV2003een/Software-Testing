import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@allure.title("Practice Test Automation Navigation Test")
@allure.description("""
This test:
- Opens https://practicetestautomation.com
- Clicks each main menu link (Practice, Blog, Courses, Contact)
- Verifies that the expected URL is opened
""")
@allure.severity(allure.severity_level.CRITICAL)
def test_practicetest_navigation():
    with allure.step("Setup Chrome WebDriver"):
        service = Service(r"C:\Users\HP\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe")
        options = Options()
        # Uncomment if you want headless:
        # options.add_argument("--headless=new")
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()

    try:
        with allure.step("Open Practice Test Automation homepage"):
            driver.get("https://practicetestautomation.com")
            time.sleep(2)
            _attach_screenshot(driver, "Home Page")

        menu_links = {
            "PRACTICE": "practice",
            "BLOG": "blog",
            "COURSES": "courses",
            "CONTACT": "contact"
        }

        for link_text, expected_url_part in menu_links.items():
            with allure.step(f"Click link: {link_text}"):
                link = driver.find_element(By.LINK_TEXT, link_text)
                link.click()
                time.sleep(2)
                current_url = driver.current_url

                allure.attach(
                    current_url,
                    name=f"URL after clicking {link_text}",
                    attachment_type=allure.attachment_type.TEXT
                )

                _attach_screenshot(driver, f"Page after clicking {link_text}")

                assert expected_url_part in current_url, f"Expected '{expected_url_part}' in URL, but got {current_url}"

                # Navigate back to home page for the next link
                driver.get("https://practicetestautomation.com")
                time.sleep(2)

        with allure.step("All menu links tested successfully."):
            allure.attach("Navigation test completed.", name="Test Status", attachment_type=allure.attachment_type.TEXT)

    finally:
        with allure.step("Close browser"):
            driver.quit()


def _attach_screenshot(driver, name):
    screenshot = driver.get_screenshot_as_png()
    allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
