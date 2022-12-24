"""
import requests
# get()获取网页
r = requests.get('https://www.baidu.com')   # r是一个<class 'requests.models.Response'>对象
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

# import requests
# # get()获取网页
# from lxml import html
# etree = html.etree
# path = "/html/body/main/div[1]/section/ul/li[1]/figure/a[2]/@href"  # 图片的xPath路径
# r = requests.get('https://wallhaven.cc/search?q'
#                  '=id:1394&sorting=random&ref=fp')   # r是一个<class 'requests.models.Response'>对象
# """
# # 检查连接状态
# if r.status_code == 200:
#     print("连接成功！")
# else:
#     print("连接失败")
# """
# e1 = etree.HTML(r.text)
# print(e1.xpath(path))
# # print("网页编码为：", r.encoding)ink)

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
# print(len(con))
# print(con[0] + con[1])

# 尝试获取wallhaven的图片
import requests
from lxml import etree
path = '//*[@id="featured"]/div[2]/span[1]/a/@href'  # 图片的xPath路径
url = 'https://wallhaven.cc/'   # 网址
r = requests.get(url)
e = etree.HTML(r.text)
link = e.xpath(path)    # 图片链接
i = 1
with open(f'./Pictures/picture({i}).jpg', 'wb') as f:
    data = requests.get(link[0])
    f.write(data.content)