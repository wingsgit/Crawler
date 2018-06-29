'''
加载短评的网址:
https://video.coral.qq.com/varticle/1003028429/comment/
v2?callback=_varticle1003028429commentv2&orinum=10&oriorder=o&pageflag=1&cursor=6194296630230283948&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=9&_=1530195424467

再点一次:
https://video.coral.qq.com/varticle/1003028429/comment/
v2?callback=_varticle1003028429commentv2&orinum=10&oriorder=o&pageflag=1&cursor=6219124941700807405&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=9&_=1530195424468

研究一下我们发现：
评论的ID对应的字段为：cursor
orinum字段对应着加载的评论数目
1003028429--代表了士兵突击的短评论编号
最简形式：
https://video.coral.qq.com/varticle/1003028429/comment/v2?callback=_varticle1003028429commentv2&orinum=10&oriorder=o&pageflag=1&cursor=6194296630230283948

"content"-->评论的内容
"nick"--昵称
nick的位置是在userList里面的..
'''
import urllib.request
import http.cookiejar
import re

def craw(videoid,commentid):
    url = "https://video.coral.qq.com/varticle/" + videoid + "/comment/v2?callback=_varticle" + videoid + "commentv2&orinum=10&oriorder=o&pageflag=1&cursor=" + commentid
    data = urllib.request.urlopen(url).read().decode("utf-8")
    return data


videoid = "1003028429"
commentid = "6194296630230283948"
url = "https://video.coral.qq.com/varticle/"+ videoid + "/comment/v2?callback=_varticle" + videoid + "commentv2&orinum=10&oriorder=o&pageflag=1&cursor=" + commentid

headers = {
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gb2312,utf-8",
    "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    "Connection":"keep-alive",
    "referer":"qq.com"
}

cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
headall = []  #建立空列表，存储头消息
for key,value in headers.items():
    item = (key,value) #变成一个元组
    headall.append(item)
opener.addheaders = headall
urllib.request.install_opener(opener)


idpat = '"id":"(.*?)",'
useridpat = ',"userid":"(.*?)",'
contentpat = '"content":"(.*?)",'

userpat = '{"userid":"(.*?)","h'

for i in range(1,6):
    print("第"+ str(i) + "页评论内容")
    data = craw(videoid,commentid)
    origin = re.compile(userpat,re.S).findall(data)
    idlist = re.compile(idpat, re.S).findall(data)
    useridlist = re.compile(useridpat).findall(data)
    contentlist = re.compile(contentpat, re.S).findall(data)
    num=[]
    nickname=[]
    for j in range(0, 10):
        num.append(re.compile('(.*?)",').findall(origin[j])[0])
        nickname.append(origin[j].split('"')[-1])
    dic = dict(zip(num,nickname))

    for k in range(0, 10):
        userid = useridlist[k]
        currentname = dic[userid]
        print("用户名为:" + eval('u"' + currentname + '"'))  # eval函数执行一个字符串表达式，并返回表达式的值
        print("评论内容为:" + eval('u"' + contentlist[k] + '"'))
        print("\n")
    commentid = idlist[9]






