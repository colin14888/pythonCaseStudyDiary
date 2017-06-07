# -*- coding:utf-8 -*-
import requests, threading
from lxml import etree
from bs4 import BeautifulSoup
import re

def get_html(url):#获得网页文件
    userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    headers = {'User-Agent':userAgent}
    req = requests.get(url= url, headers=headers)#伪装完后的请求
    response= req.content
    return response

url = 'http://www.juekong.com/meinv/1634_2.htm'
soup2= BeautifulSoup(get_html(url),'lxml')
    #总页数
pageN = soup2.find('h1')
pageN = re.split('/',str(pageN))[1]
pageN = re.split('\)',pageN)[0]
print pageN