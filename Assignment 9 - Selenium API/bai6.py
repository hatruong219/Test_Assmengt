from selenium import webdriver
from urllib.request import urlopen
import time

chrome_driver_path = "C:\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://practice.automationtesting.in/")
driver.set_window_size(1500, 1000)

page_content = urlopen('http://practice.automationtesting.in').read()
try:
    with open('page_content.html', 'wb') as fid:
        fid.write(page_content)
except Exception as e:
    print(e)
finally:
    driver.close()
