'''
1.去除&amp;字符串，否则微信公众号网址会报错
2.需要使用代理服务器的方式来解决屏蔽IP的问题
规划如下：
1.函数：代理服务器爬取指定网址并返回数据  函数：获取多个页面所有的文章链接  函数：实现根据链接爬取标题和内容并能进行本地存储
2.代理服务器需要建立异常处理机制
3,对关键词使用urllib.request.quote进行编码，构造出对应的文章列表页地址
4.代码异常需要进行延时处理
'''
import re
import urllib.request
import time
import urllib.error

headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)

listurl = []  #设置一个列表listurl存储文章网址列表



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



def getlisturl(key,pagestart,pageend,proxy):
    try:
        page = pagestart
        keycode = urllib.request.quote(key)  #编码关键词key
        for page in range(pagestart,pageend+1):
            url="http://weixin.sogou.com/weixin?type=2&query=" + keycode + "&page=" + str(page)
            data_link = use_proxy(proxy,url)  #使用代理，防止被封IP
            listurlpat = '<div class="txt-box">.*?(http://.*?)"'  #正则表达式获取文章链接
            listurl.append(re.compile(listurlpat,re.S).findall(data_link)) #放入列表中
        print("共获取到"+ str(len(listurl)) + "页" )
        return listurl

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        time.sleep(10)  # 若有异常，延时10秒
    except Exception as e:
        print("exception:" + str(e))
        time.sleep(1)

def getcontent(listurl,proxy):
    fh = open("D://666.txt","wb")
    #listurl是二维列表，第一维存储信息在第几页，第二维存储该页第几个文章的信息
    for i in range(0,len(listurl)):
        for j in range(0,len(listurl[i])):
            try:
                url = listurl[i][j]
                url = url.replace("amp;","")
                data = use_proxy(proxy,url)

                titlepat = "<title>(.*?)</title>"
                contentpat = 'id="js_content">(.*?)id="js_sg_bar"'
                title = re.compile(titlepat).findall(data)
                content = re.compile(contentpat,re.S).findall(data)
                thistitle = "no"
                thiscontent ="no"
                if(title!=[]):
                    thistitle=title[0]
                if(content!=[]):
                    thiscontent=content[0]
                dataall = "标题为"+ thistitle +"\n"+"内容为:"+ thiscontent
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




key = "西南交通大学"
proxy = "119.6.136.122:80"
pagestart = 1
pageend = 2
listurl = getlisturl(key,pagestart,pageend,proxy)
getcontent(listurl,proxy)

