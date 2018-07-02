import scrapy
from myfirstpjt.items import MyfirstpjtItem

class WeisuenSpider(scrapy.Spider):
    # name = "weisuen" #爬虫名称
    # allowed_domains = ["iqianyue.com"] #允许爬行的域名
    # start_urls = ('http://www.iqianyue.com/',) #爬行的起始地址
    # def parse(self,response): #处理Scrapy爬虫爬行到的网页相应(response)的默认方法，响应处理并返回处理后的数据
    #     pass


    '''
    name = "weisuen" #爬虫名称
    allowed_domains = ["sina.com.cn"] #允许爬行的域名
    start_urls = (
        'http://sports.sina.com.cn/basketball/nba/2018-07-02/doc-ihespqry3423342.shtml',
        'http://news.sina.com.cn/w/2018-07-02/doc-ihespqry1885531.shtml',
        'http://sc.sina.com.cn/news/b/2018-07-02/detail-ihespqry3438703.shtml',
    )
    def parse(self,response):
        item = MyfirstpjtItem()
        item['urlname'] = response.xpath("/html/head/title/text()")
        print(item["urlname"])
    '''
    name = "weisuen"  # 爬虫名称
    start_urls = (
        'http://sports.sina.com.cn/basketball/nba/2018-07-02/doc-ihespqry3423342.shtml',
        'http://news.sina.com.cn/w/2018-07-02/doc-ihespqry1885531.shtml',
        'http://sc.sina.com.cn/news/b/2018-07-02/detail-ihespqry3438703.shtml',
    )
    url2 = (
        "http://www.jd.com",
        "http://sina.com.cn",
        "http://yum.iqianyue.com"
    )
    #重写了start_requests方法
    def start_requests(self):
        for url in self.url2:
            yield self.make_requests_from_url(url)
    def parse(self, response):
        item = MyfirstpjtItem()
        item["urlname"] = response.xpath("/html/head/title/text()")
        print(item["urlname"])
        
