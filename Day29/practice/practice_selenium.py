import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

os.environ['PATH'] += r"C:/Program Files (x86)"

browser=webdriver.Chrome()
browser.get("https://www.newegg.ca/")
time.sleep(3)
browser.find_element(By.TAG_NAME,"input").send_keys("typing",Keys.RETURN)

# browser.close()

