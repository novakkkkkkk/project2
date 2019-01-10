from selenium import webdriver
#导入selenium中的actionchains的方法
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome("F:\driver\chromedriver_win32\chromedriver.exe")
time.sleep(3)
driver.get("https://www.baidu.com")
driver.maximize_window()
time.sleep(3)
#识别需要悬停的元素
ele = driver.find_element_by_xpath("//*[@id='u1']/a[9]")
#鼠标移到悬停元素上
ActionChains(driver).move_to_element(ele).perform()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='head']/div/div[4]/div/div[2]/div[1]/div/a[2]/span").click()
driver.quit()


