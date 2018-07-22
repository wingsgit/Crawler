# 大多数现代web应用都使用了AJAX技术。当浏览器加载一个页面的时候，该页面内的元素可能在不同的时间间隔内进行加载。
# 这使得元素定位变得比较困难：如果一个元素还没有出现在DOM中，定位函数将会抛出一个ElementNotVisibleException异常。
# 使用waits等待可以解决这个问题。等待将会给定位一个元素或者对元素进行一些其他的操作提供一个缓冲的时间。
#其中应用了显性等待。程序每隔xx秒看一眼，如果条件成立了，则执行下一步，否则继续等待，直到超过设置的最长时间，然后抛出TimeoutException。

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re
from lxml import etree
import MySQLdb as db

global browser
global wait
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)  # 显性等待

def search():
    try:
        browser.get("https://www.taobao.com") #打开请求的URL
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"#q"))
        ) #等待搜索输入框加载完成 presence_of_element_located 判断某个元素是否被加到了dom树里
        input.send_keys("ipad")
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"#J_TSearchForm > div.search-button > button"))
        )
        submit.click()
        total = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.total'))
        )
        return total.text
    except TimeoutException:
        return search


def next_page(page_number):
    try:
        print("正在翻页:",page_number)
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > input'))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit"))
        )
        input.clear()
        input.send_keys(page_number)
        submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(page_number))
            ##判断str(page_number)是否在文本中(是的话会高亮）
        )#text_to_be_present_in_element 判断某个元素中的text是否包含了预期的字符串
        get_products()
    except TimeoutException:
        return next_page(page_number)







def get_products():
    wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="mainsrp-itemlist"]'))
    )
    html = etree.HTML(browser.page_source)
    image_link = html.xpath("//img[@class='J_ItemPic img']/@data-src")
    price = html.xpath("//div[@class='price g_price g_price-highlight']/strong/text()")
    for j in range(len(image_link)):
        print("图像链接：",image_link[j])
        print("价格：",price[j])
    #数据库存储
        conn = db.connect('localhost', 'root', 'awpak47m4a1', 'cat_eye', charset='utf8', use_unicode=True)  # 建立mysql连接
        cur = conn.cursor()  # 数据库游标
        insert_sql = "insert into taobao(image_link,price) VALUE (%s,%s)"
        cur.execute(insert_sql, (image_link[j], price[j]))
        cur.close()
        conn.commit()
        conn.close()


def main():
    total = search()
    total = int(re.compile('(\d+)').search(total).group(1)  )  #match---by group---str total=100
    for i in range(2,11):
        next_page(i)

if __name__ == "__main__":
    main()