# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from myxml.items import MyxmlItem

class MyxmlspiderSpider(XMLFeedSpider):
    name = 'myxmlspider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/rss/1615888477.xml']
    iterator = 'iternodes' # you can change this; see the docs（迭代器设置）
    itertag = 'rss' # change it accordingly（设置开始迭代的节点）

    def parse_node(self, response, node):
        i = MyxmlItem()
        i['title'] = node.xpath("/rss/channel/item/title/text()").extract()
        i['link'] = node.xpath("/rss/channel/item/link/text()").extract()
        i['author'] = node.xpath("/rss/channel/item/author/text()").extract()
        for j in range(len(i['title'])):
            print("第"+str(j+1)+"篇文章")
            print("标题是：")
            print(i['title'][j])
            print("对应链接是:")
            print(i["link"][j])
            print("对应作者是:")
            print(i["author"][j])
            print("-----------------")
        return i
