import unittest

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from day5.myTestCase import MyTestCase
from day6.DBconnection import DBConnection


class RegisterTest(MyTestCase):
    def test_register(self):
        #数据库
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element(By.NAME, "username").send_keys("zhile0624")
        driver.find_element(By.NAME, "password").send_keys("123456")
        driver.find_element(By.NAME, 'userpassword2').send_keys("123456")
        driver.find_element(By.NAME, 'mobile_phone').send_keys("13636944868")
        driver.find_element(By.NAME, 'email').send_keys("125525@qq.com")
        driver.find_element(By.CLASS_NAME,"reg_btn").click()
        time.sleep(20)
        new_record = DBConnection().execute_sql_conmmand()
        self.assertEqual("zhile0624",new_record[1])
        print(new_record)
#if __name__ == '__main__':
#    RegisterTest.countTestCases()