# @Time : 2021/6/6 6:11 下午
# @Author : Bais
# @Email : 17343001493@163.com
# @File : test_login.py
import unittest
from time import sleep
from ddt import ddt, data, unpack, file_data
from utils import DriverUtils

from page.login_page import LoginProxy


@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_proxy = LoginProxy()

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtils.quit_driver()

    # @data(["15311093062", "hu88825889"],["15311093062", "h825889"])
    # @unpack
    @file_data("../data/login_data.yaml")
    def test_login(self, **kwargs):
        phone = kwargs.get('phone')
        pwd = kwargs.get('pwd')

        self.login_proxy.login(phone, pwd)
        sleep(2)


if __name__ == '__main__':
    unittest.main()
