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

# 尝试获取wallhaven的图片
# import requests
# from lxml import html
# etree = html.etree      # python3.5之后的 lxml 库中不能直接引入etree模块，新的版本无法直接使用“from lxml import etree”
# xPath = "//*[@id=\"thumbs\"]/section/ul/li[1]"  # 图片的xPath路径
# url = "https://wallhaven.cc/search?q=id:65348&sorting=random&ref=fp"    # 网址
# r = requests.get('https://www.baidu.com').text
# print(r)

import requests
# get()获取网页
from lxml import html
r = requests.get('https://wallhaven.cc/search?q='
                 'id:65348&sorting=random&ref=fp')   # r是一个<class 'requests.models.Response'>对象
# 检查连接状态
if r.status_code == 200:
    print("连接成功！")
else:
    print("连接失败")
text = r.text       # 字符串形式的网页源码
# print("网页编码为：", r.encoding)
