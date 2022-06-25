import os
import chromedriver_autoinstaller
from selenium import webdriver 

os.environ['PATH'] += r"C:/selenium-drivers/chromedriver.exe"
driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")
my_element = driver.find_element_by_id('downloadButton')
my_element.click()

