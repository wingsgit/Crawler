import re
import urllib.request

def getcontent(url,page):
    #模拟成浏览器,并将opener安装成全局
    headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode("utf-8") #因为有中文，所以需要编码

    userpat ='<h2>(.+?)</h2>'
    contentpat = '<div class="content">\n<span>(.*?)</span>'  #寻找出所有的内容

    userlist = re.compile(userpat,re.S).findall(data)
    contentlist = re.compile(contentpat,re.S).findall(data)
    p = 0
    for content in contentlist:
        content = content.replace("\n","")
        contentlist[p] = content
        p+=1
    q = 0
    for user in userlist:
        user = user.replace("\n", "")
        userlist[q] = user
        q += 1

    for i in range(0,len(contentlist)):
        print("用户("+"第"+str(page)+"页序号"+str(i)+")是:"+ userlist[i])
        print("内容是:")
        print(contentlist[i])


for i in range(1,3):
    url = "https://www.qiushibaike.com/8hr/page/"+ str(i)
    getcontent(url,i)

