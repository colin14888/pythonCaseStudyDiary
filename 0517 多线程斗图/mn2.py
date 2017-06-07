# -*- coding:utf-8 -*-
import requests, threading
from lxml import etree
from bs4 import BeautifulSoup
import re

#获取源码
def get_html(url):#获得网页文件
    userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    headers = {'User-Agent':userAgent}
    req = requests.get(url= url, headers=headers)#伪装完后的请求
    response= req.content
    return response