# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb as db
import urllib.request
import re

class MaoyanpjtPipeline(object):
    def __init__(self):
        self.conn = db.connect('localhost', 'root', 'awpak47m4a1', 'cat_eye', charset='utf8',use_unicode=True)  # 建立mysql连接
        print(self.conn)
        print("database connect success!")
        self.cursor = self.conn.cursor()  # 建立游标

    def process_item(self, item, spider):
        for j in range(0, len(item["name"])):
            rank = item["rank"][j]
            name = item["name"][j]
            movie_image = item["movie_image"][j]  #图片链接
            actor = item["actor"][j].replace("\n","").replace(" ","")[3:]
            uptime = item["uptime"][j][5:]
            point = str(item["integer"][j]) + str(item["fraction"][j])
            link = str("maoyan.com")+ item["link"][j]

            insert_sql = "insert into mymaoyan(rank,name,movie_image,actor,uptime,point,link) VALUE (%s,%s,%s,%s,%s,%s,%s)"
            self.cursor.execute(insert_sql, (rank,name,movie_image,actor,uptime,point,link))
            self.conn.commit()

            localpath = "./images/"+ str(item['name'][j])+'.jpg'
            urllib.request.urlretrieve(movie_image,filename=localpath)

        return item
