# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HexunpjtItem(scrapy.Item):
    name = scrapy.Field()  #文章名字
    url = scrapy.Field() #文章网址
    hits = scrapy.Field() #文章阅读数
    comment = scrapy.Field() #文章评论数
    pass
