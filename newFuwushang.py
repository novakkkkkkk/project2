from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome("F:\driver\chromedriver_win32\chromedriver.exe")
time.sleep(3)
driver.get("http://120.79.59.41/#/login")
driver.maximize_window()
time.sleep(3)
#登录
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[1]/div/div/div[1]/input").send_keys("金康高科华中区")
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[2]/div/div/div[1]/input").send_keys("admin")
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[3]/div/div/div[1]/input").send_keys("123456")
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div[2]/button/span").click()
time.sleep(3)
#点击组织管理->服务商管理菜单
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div/ul/li[2]/a").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='menu_left']/ul/li[1]/a").click()
#点击新建服务商按钮
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[1]/button/span").click()
time.sleep(5)
#输入服务商的基本信息
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[1]/div/div/input").send_keys("成都思迅中思科技有限公司")
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[2]/div/div[1]/input").send_keys("HX成都中思科技1")
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[3]/div/div/input").send_keys("思迅")
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[4]/div/div/input").send_keys("肖磊")
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[5]/div/div/input").send_keys("15012345678")
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[6]/div/div[1]/div[1]/span").click()
time.sleep(3)
#输入省份信息
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[6]/div/div[1]/div[1]/div/ul/li[1]").click()
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[1]/form/div[6]/div/div[2]/div/input").send_keys("天安门广场")
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[2]/form/div/div/div/label[2]/span[1]/span").click()
driver.find_element_by_xpath("//*[@id='companyinfos_box']/div[3]/div/button/span").click()
time.sleep(3)
#点击下一步按钮
driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/div/div[1]/div[2]/form/div[2]/div[3]/div/button/span").click()
time.sleep(3)
#输入服务商的账号信息
driver.find_element_by_xpath("//*[@id='newnumber_box']/div[1]/form/div[4]/div/div[1]/input").send_keys("ceshi999")
driver.find_element_by_xpath("//*[@id='newnumber_box']/div[1]/form/div[5]/div/div/input").send_keys("123456")
driver.find_element_by_xpath("//*[@id='newnumber_box']/div[1]/form/div[6]/div/div/input").send_keys("123456")
driver.find_element_by_xpath("//*[@id='newnumber_box']/div[1]/form/div[7]/div/div/input").send_keys("张三")
driver.find_element_by_xpath("//*[@id='newnumber_box']/div[2]/div/button/span").click()
time.sleep(5)
#退出登录
a=driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div/div/div[2]/ul/li/a[1]")
ActionChains(driver).move_to_element(a).perform()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div/div/div[2]/ul/li/a[2]").click()
time.sleep(5)

