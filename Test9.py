from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

jorney_button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
jorney_button.click()

alert = browser.switch_to.alert.accept()

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

input = browser.find_element(By.ID, "answer")
input.send_keys(y)

button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()

time.sleep(30)
browser.quit()