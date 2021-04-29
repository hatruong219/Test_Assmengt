from selenium import webdriver
# from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.maximize_window()
driver.get("https://itmscoaching.herokuapp.com/form")

# enter data to form
driver.find_element_by_id('first-name').send_keys('Binh')
driver.find_element_by_id('last-name').send_keys('Nguyen')
driver.find_element_by_id('job-title').send_keys('Tester')
driver.find_element_by_id('radio-button-3').click()
driver.find_element_by_id('checkbox-2').click()

exp = driver.find_element_by_id('select-menu')
# for option in exp.find_elements_by_tag_name('option'):
#     if option.text == '5-9':
#         option.click()
#         break

driver.find_element_by_xpath(
    "//select[@id='select-menu']//option[@value=3][text()='5-9']").click()

driver.find_element_by_id("datepicker").click()
driver.find_element_by_xpath("//th[@class='datepicker-switch']").click()
driver.find_element_by_xpath(
    "//th[@class='datepicker-switch'][text()=2021]").click()
driver.find_element_by_xpath(
    "//div[@class='datepicker-years']//th[@class='prev']").click()
driver.find_element_by_xpath(
    "//div[@class='datepicker-years']//span[text()='2011']").click()
driver.find_element_by_xpath(
    "//table[@class='table-condensed']//span[text()='Jul']").click()
driver.find_element_by_xpath(
    "//table[@class='table-condensed']//tbody//tr//td[text()=20]").click()
time.sleep(5)
driver.find_element_by_xpath("//a[@role='button'][@href='/thanks']").click()
time.sleep(2)

driver.close()
