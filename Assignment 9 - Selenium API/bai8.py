from selenium import webdriver
import time

chrome_driver_path = "C:\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")

# open login page
driver.find_element_by_xpath("//a[@href='/login']").click()

# type username and password
username_element = driver.find_element_by_id('username')
username_element.send_keys('tomsmith')
time.sleep(1)
pass_element = driver.find_element_by_id('password')
pass_element.send_keys('SuperSecretPassword!')
pass_element.submit()

print(driver.title)

time.sleep(2)
driver.close()
