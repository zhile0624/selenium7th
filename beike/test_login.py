import sys
import time

from selenium import webdriver

from test_cases.single_process.test_login_re import test_login1

import unittest
class test_login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    # @unittest.skip("test_loginCase_001")
    def test_loginCase_001(self):
        print(sys._getframe().f_code.co_name)
        print("hello world")
        test = test_login1()
        test.driver = self.driver
        test.loginame = ''
        test.login()
        test.xpath = '//*[@id="app"]/div[6]'#div弹出框
        test.style1 = "display: block"
        test.dom_panduan()#判断style=“display ：block”

        #判断用例执行结果

    # @unittest.skip("test_loginCase_002")
    def test_loginCase_002(self):#执行结果显示 ：登录账号与密码不符
        print(sys._getframe().f_code.co_name)
        test = test_login1()
        test.driver = self.driver
        test.loginame = '18713567520'
        test.style1 = "display: inline-block"
        test.xpath = '//*[@id="app"]/div[3]/div/div/div[2]/div[1]/p'
        test.login() #s输入
        test.dom_panduan()  # 判断style=“display ：block”

    # @unittest.skip("test_loginCase_003")
    def test_loginCase_003(self):#执行结果显示 ：登录账号与密码不符
        print(sys._getframe().f_code.co_name)
        test = test_login1()
        test.driver = self.driver
        test.xpath = '//*[@id="app"]/div[3]/div/div/div[2]/div[1]/p'
        test.style1 = "display: inline-block"
        test.loginpwd = r'WT-123456 '
        test.login()#s输入
        test.dom_panduan()  # 判断style=“display ：block”

    # @unittest.skip("test_loginCase_004")
    def test_loginCase_004(self):
        print(sys._getframe().f_code.co_name)
        test = test_login1()
        test.driver = self.driver
        test.xpath = '//*[@id="app"]/div[3]/div/div/div[2]/div[1]/p'

        test.style1 = "display: inline-block"
        test.loginpwd = r' WT-123456'
        test.login()#s输入
        test.dom_panduan()  # 判断style=“display ：block”


    # 5.    密码为空，其他信息正常输入，点【登录】
    # @unittest.skip("test_loginCase_005")
    def test_loginCase_005(self):
        print(sys._getframe().f_code.co_name)
        # // *[ @ id = "app"] / div[6]
        test = test_login1()
        test.driver = self.driver
        test.xpath = '//*[@id="app"]/div[6]'
        test.style1 = 'display: block'
        test.loginpwd = r''
        test.login()
        test.dom_panduan()
        print("wait.....")
        time.sleep(10000)

    # 验证码输入少一位，其他信息输入正确，点【登录】
    # @unittest.skip("test_loginCase_006")
    def test_loginCase_006(self):#延增吗相关取消
        print(sys._getframe().f_code.co_name)
        test = test_login1()
        test.driver = self.driver
        test.yanzheng = r'123'
        test.login()
        time.sleep(1000)


    # 登录成功长时间不操作，再进行操作
    def test_loginCase_007(self):
        print(sys._getframe().f_code.co_name)
        pass


if __name__ == '__main__':
    unittest.main()
