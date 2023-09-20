from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

input = browser.find_element(By.ID, "answer")
input.send_keys(y)

browser.execute_script("window.scrollBy(0, 100);")

checkbox = browser.find_element(By.ID, "robotCheckbox")
checkbox.click()

radio = browser.find_element(By.ID, "robotsRule")
radio.click()

button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()

time.sleep(30)
browser.quit()