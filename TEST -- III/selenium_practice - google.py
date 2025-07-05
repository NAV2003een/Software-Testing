from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service = Service(r"C:\Users\Administrator\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com/")
print("Successfully")
driver.quit()
