# @Time : 2021/6/6 5:28 下午
# @Author : Bais
# @Email : 17343001493@163.com
# @File : utils.py
from selenium import webdriver


#  驱动工具类
class DriverUtils:
    __driver = None

    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.get("https://passport.bilibili.com/login?from_spm_id=333.851.top_bar.login")
            cls.__driver.find_element_by_xpath('//*[@id="geetest-wrap"]/div/div[1]/span[1]').click()
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        cls.__driver.quit()
