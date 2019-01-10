from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
import unittest,time

class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome("F:\driver\chromedriver_win32\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url="https://www.baidu.com"


    def test_baidu_ide(self):
         driver =self.driver
         driver.get(self.base_url)
         driver.find_element_by_id("kw").clear()
         driver.find_element_by_id("kw").send_keys("HTMLTestRunner")
         driver.find_element_by_id("su").click()
         time.sleep(5)
         self.assertEqual(u"HTMLTestRunner_百度搜索",driver.title)


    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":

       testsuit= unittest.TestSuite()
       testsuit.addTest(BaiduTest("test_baidu_ide"))
       #定义测试报告存放路径
       fp=open("F:\HtmlTestRunner","wb")
       #定义测试报告
       runner=HTMLTestRunner(stream=fp,title="自动化测试报告",description="用例执行情况")
       runner.run(testsuit)
       #关闭测试报告
       fp.close()

