# -*- coding: utf-8 -*-
#//span[@class="ArticleTitleText"]/a/text()  --name
#//span[@class="ArticleTitleText"]/@href  --link
#function $(dvid,va){if(document.getElementById(dvid)){document.getElementById(dvid).innerHTML=va;}}$('click111757611','1125');
#文章阅读数的re:   "click\d*?','(\d*?)'"
#评论数的re:  "comment\d*?','(\d*?)'"
#对应的网址的re: '<script type="text/javascript" src=" (http://click.tool.hexun.com/.*?) ">'
#(1)提取存储评论和阅读数的网址-->(2)urllib.request爬取网址中的数据-->(3)从数据中提取阅读数和评论数

import scrapy
import re
import urllib.request
from hexunpjt.items import HexunpjtItem
from scrapy.http import Request


class MyhexunspdSpider(scrapy.Spider):
    name = 'myhexunspd'
    allowed_domains = ['hexun.com']
    uid = "fjrs168"
    #start_urls = ['http://hexun.com/']，我们重写strat_request方法，首次爬取伪装成模拟器进行
    def start_requests(self):
        yield Request("http://"+str(self.uid)+".blog.hexun.com/p1/default.html",headers=
        {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"}) #字典

    def parse(self, response):
        item = HexunpjtItem()
        item["name"] = response.xpath("//span[@class='ArticleTitleText']/a/text()").extract()
        item["url"] = response.xpath("//span[@class='ArticleTitleText']/a/@href").extract()
        pat1 = '<script type="text/javascript" src="(http://click.tool.hexun.com/.*?)">' #提取存储参数的网址
        hcurl = re.compile(pat1).findall(str(response.body))[0]
        header2 =  ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36") #元组
        opener = urllib.request.build_opener()
        opener.addheaders = [header2]
        urllib.request.install_opener(opener)

        data = urllib.request.urlopen(hcurl).read() #数据
        pat2 = "click\d*?','(\d*?)'"
        pat3 = "comment\d*?','(\d*?)'"
        item["hits"] = re.compile(pat2).findall(str(data))
        item["comment"] = re.compile(pat3).findall(str(data))
        yield item

        pat4 = "blog.hexun.com/p(.*?)/"
        data2 = re.compile(pat4).findall(str(response.body))  #获得一个列表
        if(len(data2)>=2):
            totalurl = data2[-2]
        else:
            totalurl= data2[0]
        for i in range(2,int(totalurl)+1):
            nexturl = "http://"+str(self.uid)+".blog.hexun.com/p"+str(i)+"/default.html"
            yield Request(nexturl,headers=
            {"User-Agent":
             "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"})


