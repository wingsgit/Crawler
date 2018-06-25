#第五章 正则表达式与Cookie的使用
import re



pattern = "yue" #普通字符作为原子
string = "http://yum.iqianyue.com"
result1 = re.search(pattern,string)
print(result1)

#通用字符作为原子
pattern = '\w\dpython\w' #67python8  u2python_

#原子表(定义一组地位平等的原子，然后匹配的时候会取该原子表中
#的任意一个原子进行匹配，地位平等[xyz]py-->xpy [^xyz]py-->apy
pattern1 = "\w\dpython[xyz]\w"
string = "abcdfphp345pythony_py"

#*******************************************************#
#下面来介绍正则表达式中的元字符，见书本第56页表5-3
#（1）任意匹配元字符：".python..." 匹配一个"python"字符前面有1位，后面有3位格式的字符
#（2）边界限制元字符："^$"
#（3）限定符：*,？,+,{n},{n,},{n,m}
# <1> py.*n-->python  <2> cd{2}-->cdd  <3>cd{2,}-->cddd(贪婪）
#（4）模式识别符："python|php"
#（5）模式单元符：小原子变成大原子


#*************************************************************#
#贪婪模式与懒惰模式
pattern1 = "p.*y" #贪婪模式
pattern2 = "p.*?y"#懒惰模式,搜索到了结尾字符，就立即停止


#*******************************************************#
#正则表达式常见函数
result = re.match(pattern,string,flag) #从源字符串的起始位置匹配一个模式
result2 = re.search(pattern,string) #从源字符串的全局中进行检索并匹配

#全局匹配函数（提取出所有符合模式的结果）[1]使用re.compile()对正则表达式进行预编译
#[2]使用findall()根据正则表达式从源字符串中将匹配的结果全部找出。
pattern = re.compile(".python.")
result = pattern.findall(string) #得到一个列表
print(result)

#re.sub() 正则表达式实现替换某些字符串的功能
pattern = "python."
result2 = re.sub(pattern,'php',string,2) #最多替换两次


#*******************************************************##*******************************************************#
#常见正则表达式的实例
#（1）将一串字符串里面以.com或.cn为域名后缀的URL网址匹配出来，过滤掉其他的
#无关信息。（"http://www.baidu.com"）
pattern = "[a-zA-Z]+://[^\s]*[.com|.cn]"
string = "<a href='http://www.baidu.com'>百度主页</a>"

#（2）匹配电话号码'021-67282636或者0000-2446444'
pattern = "\d{4}-\d{7} | \d{3}-\d{8}"

#（3）匹配电子邮件地址 'c-e+o@iqi-anyue.com.cn'
pattern = "\w+([.+-]\w+)*@\w+([.-]\w+)*\.\w+([.-]\w+)*"

#*******************************************************#
#Cookie(1.通过Cookie保存会话信息[会话信息保存在客户端]，
# (2.通过Session保存会话信息,服务器端保存，发送SessionID等信息）
#登录成功后，爬取该网站的其他网页时，仍会保持登录状态进行内容的爬取
import urllib.request
import urllib.parse
import http.cookiejar

url = "..." #post网址
postdata = urllib.parse.urlencode(
    {
        'username':"weisuen",
        'password':"aA123456"
    }
).encode("utf-8") #使用urlencode编码处理后，再设置为utf-8编码
req = urllib.request.Request(url,postdata) #构建Request对象
req.add_header("User-Agent","...") #模拟登录
data = urllib.request.urlopen(req).read() #登录并爬取对应网页

url2 = "..." #设置要爬取的该网站下的其他网页地址
req2 = urllib.request.Request(url2,postdata) #构建Request对象
req2.add_header("User-Agent","...") #模拟登录
data2 = urllib.request.urlopen(req2).read() #登录并爬取对应网页

####无Cookie登录，无法进行爬取data2
#(1)导入http.cookiejar
#(2)使用http.cookiejar.CookieJar()创建一个CookieJar对象
#(3)使用HTTPCookieProcessor创建cookie处理器，并以其为参数创建opener对象
#(4)创建全局默认的opener对象

url = "..." #post网址
postdata = urllib.parse.urlencode(
    {
        'username':"weisuen",
        'password':"aA123456"
    }
).encode("utf-8") #使用urlencode编码处理后，再设置为utf-8编码
req = urllib.request.Request(url,postdata) #构建Request对象
req.add_header("User-Agent","...") #模拟登录

cjar = http.cookiejar.CookieJar() #创建CookieJar对象
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
#(3)
urllib.request.install_opener(opener)#(4)
data = opener.open(req).read() #处理opener对象，使用urlopen()时，也会使用我们安装的opener对象












