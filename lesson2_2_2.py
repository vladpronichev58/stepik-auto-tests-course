from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link2 = "http://suninjuly.github.io/execute_script.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
	browser = webdriver.Chrome()
	browser.get(link2)

	x_el  = browser.find_element_by_id("input_value").text
	print(x_el)
	res = calc(x_el)
	print(res)
	
	browser.execute_script("window.scrollBy(0, 100);")
	
	answer  = browser.find_element_by_id("answer")
	answer.send_keys(res)

	option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
	option1.click()

	option2 = browser.find_element_by_css_selector("[for='robotsRule']")
	option2.click()
	
	button = browser.find_element_by_css_selector("button.btn")
	button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла