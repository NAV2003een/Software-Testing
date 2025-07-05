from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")

firstname=driver.find_element(By.XPATH,"(//input[@type='text'])[1]")
firstname.send_keys("Vimal")
time.sleep(2)
secname=driver.find_element(By.XPATH,"(//input[@type='text'])[2]").send_keys("raj")
time.sleep(2)

email=driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("sjfniouef@fowi.com")

number=driver.find_element(By.XPATH,"(//input[@type='text'])[4]").send_keys("6494987")

dob=driver.find_element(By.XPATH,"(//input[@type='text'])[5]").send_keys("27 nov 2004")


male=driver.find_element(By.XPATH,"//label[text()='Male']").click()
time.sleep(2)
driver.quit()