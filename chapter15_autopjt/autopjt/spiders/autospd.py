# -*- coding: utf-8 -*-
#当当网的笔记本网址为 http://category.dangdang.com/cid4001075.html
#第二页的网址为：http://category.dangdang.com/pg2-cid4001075.html
#xpath表达式：//a[@class="pic"]/@title  提取网页中所有class属性为pic的a标签中的title属性所对应的值
#//span[@class="price_n"]/text()
#//a[@class="pic"]/@href
#//a[@class="itemlist-review"]/text()

import scrapy
from autopjt.items import AutopjtItem
from scrapy.http import Request


class AutospdSpider(scrapy.Spider):
    name = 'autospd'
    allowed_domains = ['dangdang.com']
    start_urls = (
        "http://category.dangdang.com/pg1-cid4001075.html",
    )

    def parse(self, response):
        item = AutopjtItem()
        item["name"] = response.xpath("//a[@class='pic']/@title").extract()
        item["price"] = response.xpath("//span[@class='price_n']/text()").extract()
        item["link"] = response.xpath("//a[@class='pic']/@href").extract()
        item["comnum"] = response.xpath("//a[@name='itemlist-review']/text()").extract()
        yield item

        for i in range(1,11):
            url = "http://category.dangdang.com/pg" + str(i) + "-cid4001075.html"
            yield Request(url,callback=self.parse) #实行自动爬取
