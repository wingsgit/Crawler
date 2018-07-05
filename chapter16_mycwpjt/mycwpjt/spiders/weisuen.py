# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from mycwpjt.items import MycwpjtItem

class WeisuenSpider(CrawlSpider):
    name = 'weisuen'
    allowed_domains = ['sohu.com']
    start_urls = ['http://sohu.com/']

    #提取链接中有'.shtml"字符串的链接，然后限制只提取搜狐官方的链接（sohu.com)
    rules = (
        Rule(LinkExtractor(allow=('www.sohu.com/a/.*'),allow_domains=('sohu.com')),callback="parse_item",follow=True),
    )

    def parse_item(self, response):
        i = MycwpjtItem()
        i['name'] = response.xpath('/html/head/title/text()').extract()
        i['link'] = response.xpath("//link[@rel='canonical']/@href").extract()
        return i
