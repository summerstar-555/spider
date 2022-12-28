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
# print(nums(con))
# print(con[0] + con[1])

# 获取wallhaven的图片
import os
import requests
from lxml import etree
import time


def print_tags():  # 输出标签
    wallhaven_url = 'https://wallhaven.cc/'
    tags_xpath = '//a[@class="tagname sfw"]/text()'
    resp = requests.get(wallhaven_url)
    element = etree.HTML(resp.text)
    list1 = element.xpath(tags_xpath)
    for tag_content in list1:
        tag_content = '#' + tag_content
        print(f"\033[0;36;40m{tag_content}\033[0m", end='  ')  # 改变字体的前景色和背景色


def image_link_process(image_link: str) -> str:
    # https://w.wallhaven.cc/full/rd/wallhaven-rddgwm.jpg
    # https://th.wallhaven.cc/small/rd/rddgwm.jpg
    if "small" in image_link:
        image_link = image_link.replace("th", "w")
        image_link = image_link.replace("small", "full")
        url_path = image_link.split("/")
        url_path[-1] = f"wallhaven-{url_path[-1]}"
        return "/".join(url_path)
    return ""


print_tags()  # 输出标签
while 1:
    tag = input("\n请输入想搜索的内容标签：")
    url = f'https://wallhaven.cc/search?q={tag}'
    small_xpath = '//img[@alt="loading"]/@data-src'  # 小图片的xpath路径
    i = 0
    j = 0
    r = requests.get(url)
    e = etree.HTML(r.text)
    small_list = e.xpath(small_xpath)  # 获取一页小图片的链接
    pic_path = f'./Pictures/{tag}/'  # 根据用户输入的标签进行创建文件夹
    if not os.path.exists(pic_path):  # 检查是否存在
        os.mkdir(pic_path)
    for link in small_list:
        full_pic = image_link_process(link)  # 全屏壁纸
        fullpic_resp = requests.get(full_pic)
        if not fullpic_resp.status_code == 200:
            i = i + 1
            print(f"找不到图片！({i})")
        else:
            j = j + 1
            print(f'下载成功{j}')
            with open(f'./Pictures/{tag}/%s.jpg' % time.time(), 'wb') as f:  # 使用时间戳命名
                f.write(fullpic_resp.content)
    print(f"一共下载了{j}张图片，下载失败的图片一共有{i}张")
    answer = input("是否退出:")
    if answer == '是':
        break
