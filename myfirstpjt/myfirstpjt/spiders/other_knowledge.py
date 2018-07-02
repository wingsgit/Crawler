'''
第一节 XPATH语句
/html/body/h2/text()  提取出h2标签中的文本信息
所以我们使用了'/'和'text()'对网页代码总的信息进行快速定位

//p 将所有<p>标签的所有信息都提取出来

<div class = "fi Logo">
<img src ="....." class="f1">

获取所有class属性值为"fi"的<img>标签的内容:
//img[@class="f1"]


第二节 Spider类参数传递
重写初始化方法 __init__(),并设置参数myurl
def __init__(self,myurl=None,*args,**kwargs):
    super(WeisuenSpider,self).__init__(*args,**kwargs)
    myurllist = myurl.split("|")
    for i in myurllist:
        print("要爬取的网址为:%s" %i)
    self.start_urls = myurllist

console: scrapy crawl weisuen -a myurl="http://www.sina.com.cn|http://yum.iqianyue.com" --nolog
'''