from selenium import webdriver
import time

chrome_driver_path = "C:\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")

# open my-account page
driver.find_element_by_css_selector("#menu-item-50 a").click()

# type email and password
email_element = driver.find_element_by_id('reg_email')
email_element.send_keys('maixuanthuong1610@gmail.com')
time.sleep(1)
pass_element = driver.find_element_by_id('reg_password')
pass_element.send_keys('Tu&123Gi^i2%8Ep')
pass_element.submit()

time.sleep(2)
driver.close()
