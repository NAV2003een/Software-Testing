from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://www.google.com")
print("Opened:", driver.title)
time.sleep(2)


driver.get("https://www.wikipedia.org")
print("Opened:", driver.title)
time.sleep(2)


driver.back()
print("Back to:", driver.title)
time.sleep(2)


driver.forward()
print("Forward to:", driver.title)
time.sleep(2)


driver.refresh()
print("Page refreshed:", driver.title)
time.sleep(2)


print("Current URL:", driver.current_url)


driver.quit()