import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("https://www.baidu.com")
driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")
driver.find_element_by_xpath("//*[@id='su']").click()

time.sleep(2)

else_string = driver.find_element_by_xpath("//*[@id='1']/h3/a").text
if else_string == "Selenium - Web Browser Automation":
    print('测试成功')
driver.quit()

