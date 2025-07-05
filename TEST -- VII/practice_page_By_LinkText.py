from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://practicetestautomation.com")

menu_links={
    "PRACTICE":"practice",
    "BLOG":"blog",
    "COURSES":"courses",
    "CONTACT":"contact"
}
for link_text,expected_url in menu_links.items():
    menu_link=driver.find_element(By.LINK_TEXT,link_text)
    menu_link.click()
    time.sleep(2)
    current_url=driver.current_url
    if expected_url in current_url:
        print(f"open {menu_links[link_text]}")
    else:
        print("dosn't open")
    driver.get("https://practicetestautomation.com")
driver.quit()
