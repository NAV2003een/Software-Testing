from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()


driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(2) 

search_box = driver.find_element(By.NAME, "q")

search_box.send_keys("Amazon")

search_box.send_keys(Keys.RETURN)

time.sleep(3)
driver.quit()