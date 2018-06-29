'''
第八章 浏览器伪装技术
没有使用反爬虫:
GET /18/0628/16/DLDBBKK50001899N.html HTTP/1.1
Accept-Encoding: identity
Host: news.163.com
User-Agent: Python-urllib/3.6
Connection: close

代码如下：
import urllib.request
import http.cookiejar
url="http://news.163.com/18/0628/16/DLDBBKK50001899N.html"
cjar = http.cookiejar.CookieJar()
proxy = urllib.request.ProxyHandler({'http':"127.0.0.1:8888"})
opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler,urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read()
fh = open("./1.txt","wb")
fh.write(data)
fh.close()

'''

import urllib.request
import http.cookiejar
url="http://news.163.com/18/0628/16/DLDBBKK50001899N.html"
headers = {
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    "Connection":"keep-alive",
    "referer":"http://www.163.com/"
}
cjar = http.cookiejar.CookieJar()
proxy = urllib.request.ProxyHandler({'http':"127.0.0.1:8888"})
opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler,urllib.request.HTTPCookieProcessor(cjar))

headall = []  #建立空列表，存储头消息
for key,value in headers.items():
    item = (key,value) #变成一个元组
    headall.append(item)
opener.addheaders = headall
urllib.request.install_opener(opener)

data = urllib.request.urlopen(url).read()
fh = open("./1.txt","wb")
fh.write(data)
fh.close()
