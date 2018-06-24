import unittest

import time

from day5.myTestCase import MyTestCase


class LoginTest(MyTestCase):
    def test_login(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element_by_id("username").send_keys("zhile")
        driver.find_element_by_id("password").send_keys("123456")
        old_title = driver.title
        driver.find_element_by_class_name("login_btn").click()
        time.sleep(10)
        new_title = driver.title
        print("旧标题"+old_title)
        print("新标题"+new_title)
        self.assertNotEqual(new_title,old_title)
if __name__ == '__main__':
    unittest.main()
