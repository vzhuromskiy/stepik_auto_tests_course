from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price_button = WebDriverWait(browser, 30).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
book_button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
book_button.click()

browser.execute_script("window.scrollBy(0, 100);")

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

input = browser.find_element(By.ID, "answer")
input.send_keys(y)

button = browser.find_element(By.ID, "solve")
button.click()

time.sleep(5)
browser.quit()