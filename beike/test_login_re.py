import sys
import time

from selenium import webdriver

# from test_cases.single_process.test_login import loginop
import unittest

from test_cases.models.function import insert_img


class test_login1():
    def __init__(self):
        # self.def_name = sys._getframe().f_code.co_name
        # print(sys._getframe().f_code.co_filename)
        self.loginame = '13522424639'
        self.loginpwd = 'JW-123456'
        self.yanzheng = '1234'
        self.username = '13522424639'
        self.xpath = ''

        self.style1 = ""

    def login(self):

        # # print(sys._getframe().f_code.co_filename)
        # loginame = '13522424639'
        # oginpwd = 'JW-123456'
        # yanzheng = '1234'
        # username = '13522424639'

        self.driver.get("http://rental.ui-tech.cn/")
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div/img').click()
        self.driver.find_element_by_css_selector('#app > div.top > div > div.pull-right > ul > li:nth-child(2) > a').click()#denglu
        self.driver.find_element_by_id("UserCode").send_keys(self.loginame)

        # self.driver.find_element_by_id("PassWord").send_keys("JW-123456")
        time.sleep(1)
        self.driver.find_element_by_id("PassWord").send_keys(self.loginpwd)
        time.sleep(1)
        self.driver.find_element_by_id("txtCode").send_keys(self.yanzheng)
        time.sleep(1)
        self.driver.find_element_by_css_selector('#btnLogin').click()
        time.sleep(5)
        # text = driver.find_element_by_css_selector(
        #     "#app > div.top > div > div.pull-right > ul > li:nth-child(2) > a").text
    def panduan(self):
        try:
            text = self.driver.find_element_by_xpath(self.xpath).text
            print(text)
            if text == self.username:
                print("测试通过")
            else:
                print("测试不通过")
                insert_img(self.driver, 'aa')
        except Exception as e:
            print(e)
            insert_img(self.driver, 'aa')
    def dom_panduan(self):
        try:
            # time.sleep()
            text = self.driver.find_element_by_xpath(self.xpath).get_attribute('style')
            print(text)
            print('1'+self.style1 ,'2'+text)
            if (self.style1 in text):
                print("测试通过")
            else:
                print("测试不通过")
        except Exception as e:
            print(e)





if __name__ == '__main__':
    test_login1().login()