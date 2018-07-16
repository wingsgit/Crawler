# -*- coding: utf-8 -*-
import scrapy
import urllib.request
from scrapy.http import Request,FormRequest



class LoginspdSpider(scrapy.Spider):
    name = 'loginspd'
    allowed_domains = ['douban.com']
    header =  {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
    }
    #start_urls = ['http://douban.com/']
    def start_requests(self):
        return [Request("https://accounts.douban.com/login", meta={"cookiejar":1}, callback=self.parse)]

    def parse(self, response):
        captcha = response.xpath('//img[@id="captcha_image"]/@src').extract()
        if len(captcha)>0:
            print("有验证码啊！")
            localpath = "./captcha_images/captcha.png"
            urllib.request.urlretrieve(captcha[0],filename=localpath)
            print("请看图片输入验证码:")
            captcha_value = input()
            data={
                "form_email":"1516018513@qq.com",
                "form_password":"^*^&^&^*^",
                "captcha-solution": captcha_value,
                "redir":"https://www.douban.com/people/181279583/"
            }
        else:
            print("没验证码啊")
            data = {
                "form_email": "1516018513@qq.com",
                "form_password": ")&*(^(&*^(^(^(",
                "redir": "https://www.douban.com/people/181279583/"
            }
        print("login in........")
        return [FormRequest.from_response(
            response,
            meta={"cookiejar": response.meta["cookiejar"]},
            headers=self.header,
            formdata=data,
            callback=self.after_login,)
        ]

    def after_login(self,response):
        print("已完成登录并爬取个人中心的数据")
        xtitle = "/html/head/title/text()"
        xnotetitle = "//div[@class='note-header pl2']/a/@title"
        xnotetime = "//div[@class='note-header pl2']//span[@class='pl']/text()"
        xnotecontent = "//div[@class='mbtr2']//div[@class='note']/text()"
        xnoteurl = "//div[@class='note-header pl2']/a/@href"

        title = response.xpath(xtitle).extract()
        notetitle = response.xpath(xnotetitle).extract()
        notetime = response.xpath(xnotetime).extract()
        notecontent = response.xpath(xnotecontent).extract()
        noteurl = response.xpath(xnoteurl).extract()

        print("网页标题是:"+title[0])
        for i in range(0,len(notetitle)):
            print("第"+ str(i+1)+"篇的信息如下:")
            print("文章标题为:"+ notetitle[i])
            print("文章发表时间为:" + notetime[i])
            print("文章内容为:" + notecontent[i])
            print("文章链接为:" + noteurl[i])
            print("******************************")




