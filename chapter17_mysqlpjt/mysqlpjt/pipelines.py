# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb as db


class MysqlpjtPipeline(object):
    def __init__(self):
        self.conn = db.connect('localhost','root','***************','*********',charset='utf8',use_unicode=True) #建立mysql连接
        print(self.conn)
        print("database connect success!")
        self.cursor = self.conn.cursor()   #建立游标


    def process_item(self, item, spider):
        name = item["name"][0]
        key = item["keywd"][0]
        insert_sql = "insert into mytb(title,keywd) VALUE (%s,%s)"
        self.cursor.execute(insert_sql,(name,key))
        #self.cursor.close()
        self.conn.commit()

