from selenium import webdriver
import time

chrome_driver_path = "C:\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://practice.automationtesting.in/")
driver.set_window_size(1500, 1000)
time.sleep(3)
driver.close()
