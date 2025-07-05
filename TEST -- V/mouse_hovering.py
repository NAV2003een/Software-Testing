from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/")
driver.maximize_window()
time.sleep(2)
menu_items = {
    "Blog": ("a[href*='blog']", "blog"),
    "Contact": ("a[href*='contact']", "contact")
}

for name, (css_selector, expected_url_part) in menu_items.items():
    try:
        link = driver.find_element(By.CSS_SELECTOR, css_selector)
        link.click()
        time.sleep(2)

        current_url = driver.current_url
        if expected_url_part in current_url:
            print("redirects correctly")
        else:
            print("does NOT redirect correctly")

        driver.get("https://practicetestautomation.com/")
        time.sleep(2)

    except Exception as e:
        print(e)

driver.quit()