from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome("F:\driver\chromedriver_win32\chromedriver.exe")
time.sleep(5)
driver.get("http://120.79.59.41/#/login")
driver.maximize_window()
time.sleep(5)
a=driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[1]/div/div/div[1]/input")
a.send_keys("金康高科")

b=driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[2]/div/div/div[1]/input")
b.send_keys("guest")

c=driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[3]/div/div/div[1]/input")
c.send_keys("789996")

d=driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div[2]/button/span")
d.click()


time.sleep(5)

driver.close()
