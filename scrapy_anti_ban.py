'''
1.禁止Cookie,禁用本地Cookies信息
在Setting.py中进行设置  # Disable cookies
COOKIES_ENABLE = False

2.设置下载延时
DOWNLOAD_DELAY = 0.7

3.使用IP池(外层列表内层字典）
IPPOOL=[
    {"ipaddr":"121.33.226.167:3128"},
    {...},
    {...}
]
设置好IP池后，需要编写下载中间件文件（HttpProxyMiddlewware)
-----middlewares.py--------

import random
from myfirstpjt.settings import IPPOOL
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware

class IPPOOLS(HttpProxyMiddleware):
    def __init__(self,ip=""):
        self.ip = ip
    def process_request(self,request,spider):  #请求处理
        thisip = random.choice(IPPOOL)
        print(this["ipaddr"])
        #将对应的IP实际添加为具体的代理，用该IP进行爬取
        request.meta["proxy"]="http://"+thisip["ipaddr"]

-----settings.py--------
DOWNLOADER_MIDDLEWARES = {
    'myfirstpjt.middlewares.IPPOOLS': 125,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':123,
}

4.使用用户代理池（User-Agent)
UAPOOL=[""."".""]

-----middlewares.py--------
import random
from myfirstpjt.settings import UAPOOL
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

class UAPOOLS(UserAgentMiddleware):
    def __init__(self,ua=""):
        self.ua = ua
    def process_request(self,request,spider):  #请求处理
        thisua = random.choice(UAPOOL)
        print(thisua)
        #将对应的IP实际添加为具体的代理，用该IP进行爬取
        request.headers.setdefault("User-Agent",thisua)

-----settings.py--------
DOWNLOADER_MIDDLEWARES = {
    'myfirstpjt.middlewares.UAPOOLS': 1,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware':2,
}

5.使用谷歌Cache,分布式爬行等等
'''

