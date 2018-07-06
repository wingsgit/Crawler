# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from mysqlpjt.items import MysqlpjtItem

class SqltestSpider(CrawlSpider):
    name = 'sqltest'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/']

    rules = (
        Rule(LinkExtractor(allow=('.*?/[0-9]{4}-[0-9]{2}-[0-9]{2}/doc-.*?shtml'), allow_domains=('sina.com.cn')), callback="parse_item",
             follow=True),
    )

    def parse_item(self, response):
        i = MysqlpjtItem()
        i['name'] = response.xpath('/html/head/title/text()').extract()
        i['keywd'] = response.xpath("/html/head/meta[@name='keywords']/@content").extract()
        return i
