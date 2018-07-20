# -*- coding: utf-8 -*-
import scrapy
from toutiaopjt.items import ToutiaopjtItem
from scrapy.http import Request
import json
import time

class ToutiaospdSpider(scrapy.Spider):
    name = 'toutiaospd'
    allowed_domains = ['toutiao.com']
    #start_urls = ['http://toutiao.com/']
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
        'x-requested-with': 'XMLHttpRequest',
    }
    def start_requests(self):
        for i in range(0,6):
            url = "https://www.toutiao.com/search_content/?offset="+ str(20*i)+ "&format=json&keyword=%E4%BD%93%E8%82%B2&autoload=true&count=20&cur_tab=1&from=search_tab"
            yield Request(url,callback=self.parse)


    def parse(self, response):
        toutiaodict = json.loads(response.text)
        toutiaocontent = toutiaodict['data']
        # print(toutiaocontent)
        for dict in toutiaocontent:
            if 'title' in dict.keys():
                item = ToutiaopjtItem()
                item['name'] = dict['title']
                item['image_link'] = dict['large_image_url']
                item['source'] = dict['source']
                #item['comment_num'] = dict['comment_count']
                item['post_time'] = dict['datetime']
                yield item







