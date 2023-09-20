from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

def sum(x, y):
  return str(int(x) + int(y))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

x_element = browser.find_element(By.ID, "num1")
x = x_element.text
y_element = browser.find_element(By.ID, "num2")
y = y_element.text

select = Select(browser.find_element(By.ID, "dropdown"))
select.select_by_value(sum(x, y))

button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
button.click()

time.sleep(10)
browser.quit()