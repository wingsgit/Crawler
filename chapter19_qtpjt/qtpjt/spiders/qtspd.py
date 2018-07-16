# -*- coding: utf-8 -*-
import scrapy
import re
from qtpjt.items import QtpjtItem
from scrapy.http import Request

class QtspdSpider(scrapy.Spider):
    name = 'qtspd'
    allowed_domains = ['58pic.com']
    start_urls = ['http://www.58pic.com/piccate/3-0-0-default-0_2_0_0_default_0-1.html']

    def parse(self, response):
        item = QtpjtItem()

        paturl = "(http://pic.qiantucdn.com/58pic/.*?/.*?/.*?/.*?.jpg!)qt324"
        item["picurl"] = re.compile(paturl).findall(str(response.body))
        patlocal = "http://pic.qiantucdn.com/58pic/.*?/.*?/.*?/(.*?).jpg"
        item["picid"] = re.compile(patlocal).findall(str(response.body))

        yield item
        for i in range(1,11):
            nexturl = "http://www.58pic.com/piccate/3-0-0-default-0_2_0_0_default_0-"+str(i)+".html"
            yield Request(nexturl,callback=self.parse)


        pass
