from selenium import webdriver
import time

driver=webdriver.Chrome("F:\driver\chromedriver_win32\chromedriver.exe")
time.sleep(3)
driver.get("https://www.baidu.com")
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='su']").click()
time.sleep(5)
driver.quit()
#测试提交代码测试提交代码




