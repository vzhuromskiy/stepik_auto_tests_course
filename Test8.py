from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

input1 = browser.find_element(By.NAME, "firstname")
input1.send_keys("Vladimir")

input2 = browser.find_element(By.NAME, "lastname")
input2.send_keys("Zhuromskiy")

input3 = browser.find_element(By.NAME, "email")
input3.send_keys("vzhuromskiy@gmail.com")

file_input = browser.find_element(By.CSS_SELECTOR, "[type='file']")
file_input.send_keys("C:/Users/vzhur/PycharmProjects/SeleniumHomeWork/vox.txt")

button = browser.find_element(By.CLASS_NAME,"btn.btn-primary")
button.click()

time.sleep(3)
browser.quit()