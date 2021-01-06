#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/31 20:39
# @Author  : william
# @Site    : 
# @File    : demo01_manyandianypaiming.py
# @Software: PyCharm

#导入使用模块函数
import requests
import re
# 定义一个获取数据页面函数：猫眼排行榜页面
def get_one_page(url,headers):
    response =requests.get(url,headers=headers)
    return response.text
#定义一个数据爬取函数模块
def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S
    )
    items = re.findall(pattern,html)
    return items
if __name__ == "__main__":
    url = "https://maoyan.com/board/4"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    # html= get_one_page(url,headers)
    result1 = parse_one_page(get_one_page(url,headers))
    print(type(result1))
    print(result1[0])