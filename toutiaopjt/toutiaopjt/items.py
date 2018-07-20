# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ToutiaopjtItem(scrapy.Item):
    name = scrapy.Field()  #新闻名字
    image_link = scrapy.Field() #图片链接
    source = scrapy.Field() #新闻来源
    comment_num = scrapy.Field() #评论数目
    post_time = scrapy.Field() #发布时间


