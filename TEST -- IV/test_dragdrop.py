import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("JQuery Drag and Drop Test")
@allure.description("""
Test performing drag-and-drop on https://jqueryui.com/droppable/
- Navigate to page
- Switch to iframe
- Drag the draggable box into droppable box
- Verify successful drop
""")
@allure.severity(allure.severity_level.CRITICAL)
def test_drag_and_drop():

    with allure.step("Setup Chrome WebDriver"):
        service = Service(r"C:\Users\HP\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe")
        options = Options()
        # REMOVE headless to test visually
        # options.add_argument("--headless=new")
        driver = webdriver.Chrome(service=service, options=options)
        driver.set_window_size(1920, 1080)

    try:
        with allure.step("Open jQuery UI Droppable page"):
            driver.maximize_window()
            driver.get("https://jqueryui.com/droppable/")
            allure.attach(driver.title, name="Page Title", attachment_type=allure.attachment_type.TEXT)
            _attach_screenshot(driver, "Initial Page")

        with allure.step("Wait for iframe and switch"):
            WebDriverWait(driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME, "demo-frame"))
            )

        with allure.step("Locate draggable and droppable elements"):
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "draggable"))
            )
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "droppable"))
            )
            source = driver.find_element(By.ID, "draggable")
            target = driver.find_element(By.ID, "droppable")

        with allure.step("Perform drag and drop action"):
            actions = ActionChains(driver)
            # Alternative to drag_and_drop:
            actions.move_to_element(source).click_and_hold().pause(1)
            actions.move_to_element(target).pause(1).release().perform()

            time.sleep(2)
            _attach_screenshot(driver, "After Drag and Drop")

        with allure.step("Verify drop was successful"):
            dropped_text = target.text
            allure.attach(dropped_text, name="Droppable Text", attachment_type=allure.attachment_type.TEXT)
            assert "Dropped" in dropped_text, f"Drag and drop failed, target text: {dropped_text}"

    finally:
        with allure.step("Close browser"):
            driver.quit()


def _attach_screenshot(driver, name):
    screenshot = driver.get_screenshot_as_png()
    allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
