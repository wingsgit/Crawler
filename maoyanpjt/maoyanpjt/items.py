# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanpjtItem(scrapy.Item):
    # define the fields for your item here like:
    rank = scrapy.Field()  # 排名
    name = scrapy.Field()  # 电影名字
    movie_image = scrapy.Field()  # 影片图像
    actor = scrapy.Field() #主演名字
    uptime = scrapy.Field() #上映时间
    integer = scrapy.Field() #得分
    fraction = scrapy.Field() #得分
    link = scrapy.Field() #影片链接

