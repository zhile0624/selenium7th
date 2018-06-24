
import ddt
import unittest
import time
from selenium import webdriver
#@ddt.ddt表示这个类实现了数据驱动
from selenium.webdriver.common.by import By

from day5.csvFileManager4 import CsvFileManager4


@ddt.ddt
class RegisterTest2(unittest.TestCase):
    #3.声明一个变量 读取CSV文件的测试数据
    data_teble=CsvFileManager4().read('test_data.csv')
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(30)
        cls.driver.quit()
  #4.为test_register方法添加装饰器@ddt.data
    #data_teble是一个list类型，包含很多元素，在data_table前加*，表示调用ddt.data()方法时，我们传入的不是列表，而是列表中的每个元素
    #所以*的作用是，把列表中的每个单独元素都单独看做成 一个参数
    @ddt.data(*data_teble)

    def test_register(self,row):

            driver = self.driver
            driver.get("http://localhost/index.php?m=user&c=public&a=reg")
            driver.find_element(By.NAME, "username").send_keys(row[0])
            driver.find_element(By.NAME, "password").send_keys(row[1])
            driver.find_element(By.NAME, 'userpassword2').send_keys(row[2])
            driver.find_element(By.NAME, 'mobile_phone').send_keys(row[3])
            driver.find_element(By.NAME, 'email').send_keys(row[4])
            check_tip = driver.find_elements(By.CSS_SELECTOR, " form > ul > li:nth-child(1) > div > span").text
            print(check_tip)
            self.assertEqual("通过信息验证！", check_tip)

if __name__ == '__main__':
    unittest.main()