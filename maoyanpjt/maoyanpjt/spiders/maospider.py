# -*- coding: utf-8 -*-
import scrapy
import urllib.request
from scrapy.http import Request
from maoyanpjt.items import MaoyanpjtItem

class MaospiderSpider(scrapy.Spider):
    name = 'maospider'
    allowed_domains = ['maoyan.com']
    #start_urls = ['http://maoyan.com/board/4?offset=0']
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"}
    def start_requests(self):
        return [Request("http://maoyan.com/board/4?offset=0",callback= self.parse)]

    def parse(self, response):
        item = MaoyanpjtItem()
        xrank = "//i[starts-with(@class,'board-index')]/text()"
        xname = "//p[@class='name']/a[@title]/text()"
        xmovie_image = "//img/@data-src"
        xactor = "//p[@class='star']/text()"
        xuptime = "//p[@class='releasetime']/text()"
        xinteger = "//i[@class='integer']/text() "
        xfraction = "//i[@class='fraction']/text()"
        xlink = "//p[@class='name']/a/@href"

        item["rank"] = response.xpath(xrank).extract()
        item["name"] = response.xpath(xname).extract()
        item["movie_image"] = response.xpath(xmovie_image).extract()
        item["actor"] = response.xpath(xactor).extract()
        item["uptime"] = response.xpath(xuptime).extract()
        item["integer"] = response.xpath(xinteger).extract()
        item["fraction"] = response.xpath(xfraction).extract()
        item["link"] = response.xpath(xlink).extract()

        yield item

        for i in range(1, 6):
            nexturl = "http://maoyan.com/board/4?offset=" + str(10*i)
            yield Request(nexturl, callback=self.parse)


