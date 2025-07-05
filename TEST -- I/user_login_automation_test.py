from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 
driver=webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
username=driver.find_element(By.ID,"username")
username.send_keys("student")
password=driver.find_element(By.ID,"password")
password.send_keys("Password123")
submit_button=driver.find_element(By.ID,"submit")
submit_button.click()
time.sleep(2)
msg=driver.find_element(By.TAG_NAME,'h1').text
if "Logged In Successfully" in msg:
    print("Login successful")
else:
    print("Login Failed")
driver.quit()