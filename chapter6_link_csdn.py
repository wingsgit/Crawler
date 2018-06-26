import re
import urllib.request

def getlink(url):
    #模拟成浏览器,并将opener安装成全局
    headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)

    file = urllib.request.urlopen(url)
    data = str(file.read())

    pat = '(https?://[^\s)";]+\.(\w|/)*)'     #http://blog.csdn.net/experts/rule.html   http://lib.csdn.net/base/go
    link = re.compile(pat).findall(data)
    link = list(set(link)) #去除重复元素
    return link

url = "http://blog.csdn.net/"
linklist = getlink(url)
for link in linklist:
    print(link[0])