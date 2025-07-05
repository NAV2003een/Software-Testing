from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Click the "Click for JS Alert" button
menu=driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
menu.click()
time.sleep(3)
alert = driver.switch_to.alert
print("Alert Text:", alert.text)
alert.accept()

result = driver.find_element(By.XPATH, "//p[@id='result']").text
print("Result message:", result)


driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
time.sleep(3)
alert=driver.switch_to.alert
print("Alrt:",alert.text)
alert.dismiss()
time.sleep(5)

result = driver.find_element(By.XPATH, "//p[@id='result']").text
print("Result message:", result)


driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
time.sleep(3)

alert=driver.switch_to.alert
print("Alert:",alert.text)
alert.send_keys("Vimal")
time.sleep(3)
alert.accept()
time.sleep(3)

result = driver.find_element(By.XPATH, "//p[@id='result']").text
print("Result message:", result)
driver.quit()
