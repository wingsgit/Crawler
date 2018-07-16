# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib.request

class QtpjtPipeline(object):
    def process_item(self, item, spider):
        for i in range(0,len(item['picurl'])):
            thisurl = item["picurl"][i] #获取当前图片网址(大图）
            localpath = "./images/"+ item["picid"][i]+".jpg"
            urllib.request.urlretrieve(thisurl,filename=localpath)
        return item
