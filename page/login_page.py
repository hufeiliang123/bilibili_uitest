# @Time : 2021/6/6 5:39 下午
# @Author : Bais
# @Email : 17343001493@163.com
# @File : login_page.py
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utils import DriverUtils


# 对象库层，找到页面中要操作元素的，定义定位元素的方法
class LoginPage:
    def __init__(self):
        self.driver = DriverUtils.get_driver()
        self.phone = (By.ID, 'login-username')
        self.pwd = (By.XPATH, '//*[@id="login-passwd"]')
        self.button = (By.XPATH, '//*[@id="geetest-wrap"]/div/div[5]/a[1]')

    def find_phone(self):
        return self.driver.find_element(self.phone[0], self.phone[1])

    def find_pwd(self):
        return self.driver.find_element(self.pwd[0], self.pwd[1])

    def find_button(self):
        return self.driver.find_element(self.button[0], self.button[1])


# 操作层：定义操作元素的方法

class LoginHandle:
    def __init__(self):
        self.login_page = LoginPage()

    def input_phone(self, phone):
        self.login_page.find_phone().clear()
        self.login_page.find_phone().send_keys(phone)
        time.sleep(2)

    def input_pwd(self, pwd):
        self.login_page.find_phone().clear()
        self.login_page.find_pwd().send_keys(pwd)
        time.sleep(2)

    def click_button(self):
        self.login_page.find_button().click()
        # self.login_page.find_button().send_keys(Keys.ENTER)


# 业务层 ，把多个操作组合成一个完整的业务流程

class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()

    def login(self, phone, pwd):
        self.login_handle.input_phone(phone)
        self.login_handle.input_pwd(pwd)
        self.login_handle.click_button()
