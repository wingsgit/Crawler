# -*- coding: utf-8 -*-
import scrapy
from mypjt.items import MypjtItem

class WeisuenSpider(scrapy.Spider):
    name = 'weisuen'
    allowed_domains = ['sina.com.cn']
    start_urls = (
        'http://sports.sina.com.cn/basketball/nba/2018-07-02/doc-ihespqry3423342.shtml',
        'http://sina.com.cn',
    )

    def parse(self, response):
        item = MypjtItem()
        item["title"] = response.xpath("/html/head/title/text()").extract()  #后面这个方法很重要，anything.xpath('...') is a selector, not a string
        item["key"] = response.xpath("//meta[@name='keywords']/@content").extract()
        #print(item["title"])
        yield item #需要有item的返回哦，不然pipeline抓不到数据