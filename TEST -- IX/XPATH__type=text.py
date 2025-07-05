from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
time.sleep(1)

first_name = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
first_name.clear()
first_name.send_keys("Mahesh")


last_name = driver.find_element(By.XPATH, "(//input[@type='text'])[2]")
last_name.clear()
last_name.send_keys("Varan")

print("All alerts handled.")
time.sleep(2)
driver.quit()