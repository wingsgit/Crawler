# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider
from mycsv.items import MycsvItem


class MycsvspiderSpider(CSVFeedSpider):
    name = 'mycsvspider'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://yum.iqianyue.com/weisuenbook/pyspd/part12/mydata.csv']
    headers = ['name', 'sex', 'addr', 'email']
    delimiter = ','

    # Do any adaptations you need here
    #def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        i = MycsvItem()
        i['name'] = row['name']
        i['sex'] = row['sex']
        print("名字是:")
        print(i['name'])
        print("性别是:")
        print(i['sex'])
        print("--------------------------------")
        #i['description'] = row['description']
        return i
