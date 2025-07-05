from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.execute_script("window.open('https://www.wikipedia.org', '_blank');")
time.sleep(2)
tabs = driver.window_handles
driver.switch_to.window(tabs[1])
print("Title:", driver.title)
driver.close()
driver.switch_to.window(tabs[0])
driver.quit()
