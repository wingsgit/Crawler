import urllib.request
import urllib.parse
import urllib.error

file = urllib.request.urlopen("http://www.baidu.com")
data = file.read() #爬取网页的全部内容,赋给一个字符串变量
datal = file.readlines() #爬取文件的全部，但赋给一个列表变量
dataline = file.readline() #爬取网页的一行内容

#通过以下代码实现将爬取到的网页保存在本地
fhandle = open("path_name","wb")
fhandle.write(data)
fhandle.close()
#方法2,直接将对应信息写入本地文件
filename = urllib.request.urlretrieve("http:www.baidu.com",filename= "local_path")
urllib.request.urlcleanup() #清除缓存

#******************************************************#

#有的时候被设置了403错误，为了反反爬虫，可以设置一些Headers信息，模拟成浏览器访问这些网站（设置user-Agent）信息

#方式1：使用urllib.request.build_opener()修改报头
url = "..."
header = ("User-Agent","...")
opener = urllib.request.build_opener() #创建自定义的opener对象并赋给变量opener
opener.addheaders =[headers] #设置opener对象的addheaders，设置对应的头信息
data = opener.open(url).read()  #使用opener对象的open()方法打开相应的网址，并read()方法读取相应数据，然后赋给data变量

#方法2，使用add_header()添加报头
url="..."
req = urllib.request.Request(url) #创建一个Request对象
req.add_header("User-Agent","..")  #添加对应的报头信息
data = urllib.request.urlopen(req).read() #打开并读取赋值

#******************************************************#
#超时设置
for i in range(1,100):
    try:
        file = urllib.request.urlopen("...",timeout=1) #超时设置为1秒
        data = file.read()
        print(len(data))
    except Exception as e:
        print("出现异常-->"+ str(e))

#*******************************************************#

# http协议请求实战
#主要的两种请求：（1）Get请求：请求通过URL网址传递信息，可以直接在URL中写上要传递的信息。表单传递也行，不过会自动转成URL中的数据，
#通过URL地址传递。（2）POST请求：可以向服务器提交数据，主流+安全，一般登录使用POST请求发送数据。

#Get请求实例分析（爬虫自动百度查询关键词为hello的结果，wd字段检索）

keywd = "hello"
url = "http://www.baidu.com/s?wd="+ keywd
req = urllib.request.Request(url)  #构建了一个Request对象并赋给变量req
data = urllib.request.urlopen(req).read() #打开了request对象，由于网址中包含了GET请求，会以GET请求的方式获取该页面

fhandle = open("path_name","wb")
fhandle.write(data)
fhandle.close()

#若出现中文，则根据编码更改
key = "的咖啡机的"
key_code = urllib.request.quote(key) #对关键词部分进行编码
url_all = url + key_code

#POST请求实例分析（爬虫自动百度查询关键词为hello的结果，wd字段检索）
url="....."
postdata = urllib.parse.urlencode(
    {
        "name":"fdskf",
        "password":"123456"
    }
).encode('utf-8') #构造表单数据，对数据进行编码处理
req = urllib.request.Request(url,postdata)#创建Request对象，参数包括URL和传递的数据
req.add_header("User-Agent","...") #添加头信息
data = urllib.request.urlopen(req).read() #打开对应的Request对象，完成信息的传递

fhandle = open("path_name","wb")
fhandle.write(data)
fhandle.close()


#*******************************************************#
#代理服务器的设置，不能一直用同一个IP爬取同一个网站上的网页（202.75.210.45:7777)
def use_proxy(proxy_addr,url):
    proxy = urllib.request.ProxyHandler({"http": proxy_addr}) #设置对应的代理服务器信息
    opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler) #创建一个自定义的opener对象
    urllib.request.install_opener(opener) #将我们自定义的opener对象，在使用urlopen()时就会直接使用我们安装的opener对象
    data = urllib.request.urlopen(url).read().decode("utf-8")
    return data
proxy_addr = "202.75.210.45:7777"
data = use_proxy(proxy_addr,"http://www.baidu.com")
print(len(data))

#*******************************************************#
#异常处理（URLError类和HTTPError类）
try:
    urllib.request.urlopen("...")
except urllib.error.URLError as e:
    if hasattr(e,"code"):  #hasattr() 函数用于判断对象是否包含对应的属性。
        print(e.code)  #403（HTTPError状态码，URLError没有这个）
    if hasattr(e,"reason"):
        print(e.reason) #Forbidden,事实上触发了HttpError






