import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://news.baidu.com')
time.sleep(1)

news_link = driver.find_element_by_xpath("//*[@id='pane-news']/div/ul/li[1]/strong/a")
page1_text = news_link.text
news_link.click()
print(driver.current_window_handle)
handles = driver.window_handles
print(handles)

for handle in handles:
    if handle != driver.current_window_handle:
        print("Switch to second window")
        driver.switch_to.window(handle)

page2_test = driver.find_element_by_xpath('//*[@id="activity-name"]').text

try:
    assert page1_text in page2_test
    print("test_success!")
except Exception as e:
    print("test_failed!!!")

