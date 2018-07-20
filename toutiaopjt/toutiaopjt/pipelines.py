# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib.request

class ToutiaopjtPipeline(object):
    def process_item(self, item, spider):
        file = open("./666.txt", "a")
        file.write(str(item))
        file.close()
        if 'image_link' in item:
            image_link = item['image_link']
            localpath = "./images/" + str(item['name']) + '.jpg'
            urllib.request.urlretrieve(image_link, filename = localpath)












