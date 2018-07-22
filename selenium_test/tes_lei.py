import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BaiduSearch(object):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    def open_beidu(self):
        self.driver.get('https://www.baidu.com')
        time.sleep(1)
    def test_search(self):
        self.driver.find_element_by_id('kw').send_keys("selenium")
        self.driver.find_element_by_id('su').send_keys(Keys.ENTER)
        time.sleep(1)
        print(self.driver.title)
        try:
            assert 'selenium_百度搜索' in self.driver.title
            print("ok")
        except Exception as e:
            print("fail")


baidu = BaiduSearch()
baidu.open_beidu()
baidu.test_search()