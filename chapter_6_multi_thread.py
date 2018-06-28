'''
所谓的多线程爬虫，某部分程序可以并行执行
可以导入threading模块使用多线程功能
需要定义一个类继承threading.Thread类，__init__(self)线程初始化，run(self）写上线程要执行的程序 start()启动线程

import threading
class A(threading.Thread):
    def __init__(self):
        threading,Thread.__init__(self)
    def run(self):
        for i in range(10)
            print("thread A")
class B(threading.Thread):
    def __init__(self):
        threading,Thread.__init__(self)
    def run(self):
        for i in range(10)
            print("thread b")
t1 = A()
t1.start()
t2 = B()
t2.start()

队列对象，可以通过put(data），将对应的数据传到队列中
a.put("hello")
a.task_done()
a.get()
需要一个总体控制的线程3，若存放网址的队列urlqueue没有了网址数据,说明线程2已经爬取完了所有的文章信息，控制退出程序
'''


import re
import urllib.request
import time
import urllib.error
import threading
import queue


headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)

urlqueue = queue.Queue()  #设置一个列表urlqueue队列来处理获得的链接
listurl = []


def use_proxy(proxy_addr,url):
    try:
        proxy = urllib.request.ProxyHandler({'http':proxy_addr})
        opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)

        data = urllib.request.urlopen(url).read().decode("utf-8")
        return data

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        time.sleep(10)  # 若有异常，延时10秒
    except Exception as e:
        print("exception:" + str(e))
        time.sleep(1)


#线程1：获取对应网址
class geturl(threading.Thread):
    def __int__(self,key,pagestart,pageend,proxy,urlqueue):
        threading.Thread.__init__(self)
        self.pagestart = pagestart
        self.pageend = pageend
        self.proxy = proxy
        self.urlqueue = urlqueue
        self.key = key
    def run(self):
        page = self.pagestart
        keycode = urllib.request.quote(self.key)  #编码关键词key
        for page in range(self.pagestart,self.pageend+1):
            url="http://weixin.sogou.com/weixin?type=2&query=" + keycode + "&page=" + str(page)
            data_link = use_proxy(self.proxy,url)  #使用代理，防止被封IP
            listurlpat = '<div class="txt-box">.*?(http://.*?)"'  #正则表达式获取文章链接
            listurl.append(re.compile(listurlpat,re.S).findall(data_link)) #放入列表中
        print("共获取到"+ str(len(listurl)) + "页" )
        for i in range(0, len(listurl)):
            time.sleep(5) #等一等线程2，合理分配资源
            for j in range(0, len(listurl[i])):
                try:
                    url = listurl[i][j]
                    url = url.replace("amp;", "")
                    self.urlqueue.put(url) #地址入队
                    self.urlqueue.task_done()
                except urllib.error.URLError as e:
                    if hasattr(e, "code"):
                        print(e.code)
                    if hasattr(e, "reason"):
                        print(e.reason)
                    time.sleep(10)  # 若有异常，延时10秒
                except Exception as e:
                    print("exception:" + str(e))
                    time.sleep(1)

#线程2,与线程1并行执行，从线程1中提供的文章地址一次爬取文章内容进行处理
class getcontent(threading.Thread):
    def __int__(self,proxy,urlqueue):
        threading.Thread.__init__(self)
        self.urlqueue = urlqueue
        self.proxy = proxy
    def run(self):
        fh = open("D://666.txt", "wb")
        while(True):
            try:
                url = self.urlqueue.get()  #从队列里抓link
                data = use_proxy(self.proxy, url)
                titlepat = "<title>(.*?)</title>"
                contentpat = 'id="js_content">(.*?)id="js_sg_bar"'
                title = re.compile(titlepat).findall(data)
                content = re.compile(contentpat, re.S).findall(data)
                thistitle = "no"
                thiscontent = "no"
                if (title != []):
                    thistitle = title[0]
                if (content != []):
                    thiscontent = content[0]
                dataall = "标题为" + thistitle + "\n" + "内容为:" + thiscontent
                fh.write(dataall.encode("utf-8"))

            except urllib.error.URLError as e:
                if hasattr(e, "code"):
                    print(e.code)
                if hasattr(e, "reason"):
                    print(e.reason)
                time.sleep(10)  # 若有异常，延时10秒
            except Exception as e:
                print("exception:" + str(e))
                time.sleep(1)
        fh.close()
#线程3：并行控制，若60秒未响应，并且uel队列空了，则判断执行成功
class conrl(threading.Thread):
    def __int__(self,urlqueue):
        threading.Thread.__init__(self)
        self.urlqueue = urlqueue
    def run(self):
        while(True):
            print("gogogo")
            time.sleep(60)
            if(self.urlqueue.empty()):
                print("done!")
                exit()

key = "西南交通大学"
proxy = "119.6.136.122:80"
pagestart = 1
pageend = 2
t1 = geturl(key,pagestart,pageend,proxy,urlqueue)
t1.start()
t2 = getcontent(urlqueue,proxy)
t2.start()
t3.start()



