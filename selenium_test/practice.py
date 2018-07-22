import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

dr = webdriver.Chrome()
dr.implicitly_wait(30)
#打开百度
dr.get('https://www.baidu.com/')
dr.find_element_by_tag_name("body")
#firefox,打开一个新的标签页(ctrl+t在这里有bug)
js = 'window.open("");'
dr.execute_script(js)
#取得标签页窗口句柄
winhandles = dr.window_handles
#切换到第二个标签页
dr.switch_to.window(winhandles[1])
dr.get("http://www.swjtu.edu.cn/")
time.sleep(3)
