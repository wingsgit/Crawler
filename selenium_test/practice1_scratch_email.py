from selenium import webdriver
import re
import time

driver = webdriver.Chrome()
driver.implicitly_wait(6)

driver.get("https://www.baidu.com")
time.sleep(1)

for link in driver.find_elements_by_xpath("//*[@href]"):
    print(link.get_attribute('id'))




# driver.get("http://news.baidu.com")
# time.sleep(1)
#
# for image in driver.find_elements_by_tag_name('img'):
#     print(image.text)
#     print(image.size)
#     print(image.tag_name)


# driver.maximize_window()
# driver.implicitly_wait(6)
#
# driver.get("http://home.baidu.com/contact.html")
#
# doc = driver.page_source
# emails = re.findall('[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+',doc) #33_.3434@434.edu.
# for email in list(set(emails)):
#     print(email)
# driver.close()

#driver.back() driver.forward()
#driver.current_url
#driver.title
