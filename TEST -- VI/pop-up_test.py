from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(1)

driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
time.sleep(1)
alert = driver.switch_to.alert
print("Simple Alert Text:", alert.text)
time.sleep(2)
alert.accept()

driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
time.sleep(1)
alert = driver.switch_to.alert
print("Confirm Alert Text:", alert.text)
time.sleep(2)
alert.dismiss()

driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
time.sleep(1)
alert = driver.switch_to.alert
print("Prompt Alert Text:", alert.text)
time.sleep(1)
alert.send_keys("Selenium Test")
time.sleep(2)
alert.accept()

print("All alerts handled.")
time.sleep(2)
driver.quit()