import re
import urllib.request
import urllib.error
import os

def craw(url,page):
    html1 = str(urllib.request.urlopen(url).read()) #读取网页全部源代码
    pat1 = '<div id="plist".+?<div class="page clearfix">'   #只取特殊标识中间的代码，其他代码全部过滤
    result1 = re.compile(pat1).findall(html1)[0] #提取所有结果并放到一个列表里面
    pat2 = '<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">' #取所有图片的模式
    imagelist = re.compile(pat2).findall(result1)

    x=1
    for imageurl in imagelist:
        imagename = "./JD_images/"+ str(page)+"_"+str(x)+".jpg"
        imageurl = "http://" + imageurl
        try:
            urllib.request.urlretrieve(imageurl,filename=imagename) #链接对应的本地存储
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                x+=1
            if hasattr(e,"reason"):
                x+=1
        x+=1

for i in range(1,11):
    url = "https://list.jd.com/list.html?cat=9987,653,655&page=" + str(i)
    craw(url,i)