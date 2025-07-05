from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://jqueryui.com/droppable/")

iframe = driver.find_element(By.CLASS_NAME, "demo-frame")
driver.switch_to.frame(iframe)

source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()
time.sleep(5)
dropped_text = target.text
if "Dropped" in dropped_text:
    print("Drag and drop successful")
else:
    print("Drag and drop failed")
driver.quit()
