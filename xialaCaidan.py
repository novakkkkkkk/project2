from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome("F:\driver\chromedriver_win32\chromedriver.exe")
driver.get("https://www.baidu.com")
time.sleep(3)
driver.maximize_window()
#鼠标移动到设置按钮
mouse = driver.find_element_by_xpath("//*[@id='u1']/a[8]")
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(3)
driver.find_element_by_link_text("搜索设置").click()
time.sleep(3)
#先定位下拉框 s = driver.find_element_by_id("nr")
#再定位选项 s.find_element_by_xpath("//*[@id='nr']/option[2]").click()

#通过selenium.webdriver.support.ui的Select进行定位
Select(driver.find_element_by_id("nr")).select_by_value("50")
time.sleep(3)
driver.quit()




