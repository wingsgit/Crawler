# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#当当网网页商品数据自动爬取
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AutopjtItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field() #存储商品名
    price = scrapy.Field() #存储商品价格
    link = scrapy.Field() #存储商品链接
    comnum = scrapy.Field() #存储商品评论数



