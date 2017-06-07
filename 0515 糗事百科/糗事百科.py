# -*- coding:utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import lxml

def getPage(Url):
    userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30'
    headers = {'User-Agent': userAgent}
    req = urllib2.Request(url=Url, headers=headers)

    try:
        response = urllib2.urlopen(req) # open website
        content = response.read()
    except Exception,e:
        content = None

    return content

articleUrl = 'http://www.qiushibaike.com/textnew/page/%d'
commentUrl = 'http://www.qiushibaike.com/article/%s'
page=0
articleFloor = 1

while True:
    raw = raw_input('enter,exit')
    if raw =='exit':
        break
    page+=1
    Url = articleUrl % page

    #获取段子内容
    articlePage = getPage(Url)
    soupArticle = BeautifulSoup(articlePage,'lxml')#解析网页
    for string in soupArticle.find_all(attrs='article block untagged mb15'):
        commentId = str(string.get('id')).strip()[11:]
        #print commentId [11:]
        print '\n'
        print articleFloor,',',string.find(attrs = 'content').get_text().strip()
        articleFloor +=1

        #get comment
        commentPage = getPage(commentUrl % commentId)
        soupComment = BeautifulSoup(commentPage,'lxml')
        commentFloor = 1
        for comment in soupComment.find_all(attrs='body'):
            print '      ',commentFloor,'楼回复:',comment.get_text()
            commentFloor += 1