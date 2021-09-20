from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link2 = "http://suninjuly.github.io/selects1.html"

try:
	browser = webdriver.Chrome()
	browser.get(link2)

	res  = int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)
	print(res)
	select = Select(browser.find_element_by_tag_name("select"))
	select.select_by_value(str(res))

	button = browser.find_element_by_css_selector("button.btn")
	button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла