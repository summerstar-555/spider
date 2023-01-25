"""
import requests
# get()获取网页
r = requests.get('https://www.baidu.com')   # r是一个'Response'对象
# 检查连接状态
print(r.status_code)                        # 200表示正常连接，非200即失败
# 检测r的类型
print(type(r))
# 获取页面的头部信息
print(r.headers)
# 输出代码
print(r.text)                               # 这里没有改变编码格式导致乱码
# 默认编码（是从头文件中分析得来的）：
print(r.encoding)
# 更精准查询（但是也不是完全正确的，是从内容分析中得来的）：
print(r.apparent_encoding)
# 把r.apparent_encoding的编码格式赋予r.encoding
r.encoding = r.apparent_encoding
# 改变编码格式变成中文
print(r.text)
"""

# 基础知识
"""
import requests
# get()获取网页
from lxml import html
etree = html.etree
path = "/html/body/main/div[1]/section/ul/li[1]/figure/a[2]/@href"  # 图片的xPath路径
r = requests.get('https://wallhaven.cc/search?q'
                 '=id:1394&sorting=random&ref=fp')   # r是一个'Response'对象
                 
# 检查连接状态
if r.status_code == 200:
    print("连接成功！")
else:
    print("连接失败")
e1 = etree.HTML(r.text)
print(e1.xpath(path))
# print("网页编码为：", r.encoding)ink)
"""

# 实例练习
# from lxml import etree
#
# html = """
# <!DOCTYPE html>
# <html>
# <head lang="en">
# <title>测试</title>
# <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
# </head>
# <body>
# <div id="content">
# <ul id="ul">
# <li>NO.1</li>
# <li>NO.2</li>
# <li>NO.3</li>
# </ul>
# <ul id="ul2">
# <li>one</li>
# <li>two</li>
# </ul>
# </div>
# <div id="url">
# <a href="http:www.58.com" title="58">58</a>
# <a href="http:www.csdn.net" title="CSDN">CSDN</a>
# </div>
# </body>
# </html>
# """
# e1 = etree.HTML(html)
# print(e1.xpath('//div[@id="content"]/ul[@id="ul"]/li'))
#
# print(e1.xpath("//div[@id='content']/ul[@id='ul2']/li/text()"))
#
# print(e1.xpath('//div[@id="url"]/a/@href'))
#
# print(e1.xpath('//div[@id="url"]/a/@title'))
# selector = etree.HTML(html)
# content = selector.xpath('//div[@id="content"]/ul[@id="ul"]/li/text()')  # 这里使用id属性来定位哪个div和ul被匹配 使用text()获取文本内容
# for i in content:
#     print(i)
#
# con = selector.xpath('//a/@href')  # 这里使用//从全文中定位符合条件的a标签，使用“@标签属性”获取a便签的href属性值
# for each in con:
#     print(each)
#
# con = selector.xpath('/html/body/div/a/@title')  # 使用绝对路径�20 <a href="http:www.csdn.2Fa/@title') #使用相对路径定位 两者效果是一样的
# print(nums(con))
# print(con[0] + con[1])


# 反爬虫，修改UA
# 导入模块
"""
import requests

url = 'http://httpbin.org/get'  # 在网站后面加了/get,向网站发送请求的命令，这个网站是一个测试网站，不止可以用来看headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0'}
html = requests.get(url, headers=headers).text
print(html)
"""

# timeout参数
# 使用get方法长时间无响应，设置timeout参数
"""
import requests

url = 'https://wallhaven.cc/'
try:
    resp = requests.get(url, timeout=0.001)
    print(resp.status_code)
except requests.exceptions.ConnectTimeout:
    print('连接超时')
"""

# 乱码问题 - 解决方案
'''
import requests
url = 'https://www.baidu.com/'
resp = requests.get(url)
print(resp.text.encode('utf-8'))        # 把字符串编译成'utf-8'的形式
print('-'*100)
print(resp.content.decode('utf-8'))     # 把字节按'utf-8'的形式解码
'''

# request的get方法传递参数
'''
def fun1():
    url = 'https://wallhaven.cc/search'
    parameter = {
        'q': 'id:123704',       # 这里不能跟着写%3A，因为这个相当于':'符号
        'categories': '111',
        'purity': '100',
        'sorting': 'random',
        'order': 'desc',
        'seed': 'lZkF6z',
        'page': '2'
    }
    resp = requests.get(url, params=parameter)
    # 使用params之后会在网址后面先添加一个'?',然后在进行填写参数
    # 所以可以将网址'？'前面的内容复制，然后再使用params填写相应的参数
    print(resp.url)
    # 等同于‘url = 'https://wallhaven.cc/search?q=id%3A123704&categories=111&purity=100&sorting=random&order=desc&seed
    # =lZkF6z&page=2'’
    resp.close()


def fun2():
    url = 'https://wallhaven.cc/search?q=id%3A123704&categories=111&purity=100&sorting=random&order=desc&seed=lZkF6z&page=2'
    resp = requests.get(url)
    resp.close()


fun1()
fun2()
'''

# 导入RequestException异常，这个异常基本上是爬取过程中所有的错误来源
'''
import requests
from requests.exceptions import RequestException


def get_one_page(url):
    response = requests.get(url)
    try:
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def main():
    url = 'http://maoyan.com/board/4'
    html = get_one_page(url)
    print(html)


if __name__ == '__main__':
    main()
'''

# url解析
'''
url = 'https%3A%2F%2Fkh4.psdcat.com%2Fplaym3u8%2F1674016397_aabbcc05_WuLiuQiS401.m3u8'


def parse(url_fuc: str):
    url_fuc = url_fuc.replace('%3A', ':')
    url_fuc = url_fuc.replace('%2F', '/')
    return url_fuc


url = parse(url)
print(url)
'''


# 使用session方法，能够带上cookie，但这个cookie是可以明文查看的
# 如果使用get方法，则需要去网站复制自己的cookie，然后再放在头部
'''
import requests

url = 'https://passport.17k.com/ck/user/login'
session = requests.session()        # 返回一个session对象，这个对象会一直带着cookie
data = {
    "loginname": "********",
    "password": "*********"}
session.post(url, data=data)
resp = session.get('https://passport.17k.com/ck/user/login')
print(resp.json())
'''


# 流式下载
'''
import requests
import os
url = 'https://video.pearvideo.com/head/20230113/cont-1718750-15952493.mp4'   # 视频的真正下载地址
file_name = os.path.split(url)[1]       # 获取文件名
resp = requests.get(url, stream=True)       # 使用流式下载
with open(f'./{file_name}', 'wb') as f:
    for chunk in resp.iter_content(chunk_size=1024):  # 一次从迭代器内部拿出1024个字节
        f.write(chunk)
'''
