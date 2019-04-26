# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb as db

class HexunpjtPipeline(object):
    def __init__(self):
        self.conn = db.connect('localhost', 'root', '*************', 'h***n', charset='utf8',
                               use_unicode=True)  # 建立mysql连接
        print(self.conn)
        print("database connect success!")
        self.cursor = self.conn.cursor()  # 建立游标

    def process_item(self, item, spider):

        for j in range(0,len(item["name"])):
            name = item["name"][j]
            url = item["url"][j]
            hits = item["hits"][j]
            comment = item["comment"][j]
            insert_sql = "insert into myhexun(name,url,hits,comment) VALUE (%s,%s,%s,%s)"
            self.cursor.execute(insert_sql, (name,url,hits,comment))
            self.conn.commit()
        return item


    def close_spider(self,spider):
        self.conn.close()











