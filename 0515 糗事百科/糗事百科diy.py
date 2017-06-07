# -*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup#python3用bs3


def getPage(Url):#获得html文件方法
    #定义User-Agent
    userAgent ='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110'
    headers = {'User-Agent':userAgent}#装进头文件
    req = urllib2.Request(url=Url,headers=headers)#合成 请求命令()
    try:#预防503错误——服务器错误()
        response = urllib2.urlopen(req)#发送 请求命令 并获得 html 文件()
        content = response.read()#html 内容读取

    except Exception,e:
        content = None
        print('nothing')
    return content #获取内容(html 文件内容)

Url1='http://www.qiushibaike.com/8hr/page/%d'
comUrl = 'http://www.qiushibaike.com/article/%s'
page = 0
articleFloor = 0
getPage(Url1 % page)
idList=[]

while page !=1:#获取1-10页
    page +=1 #迭代页码
    Url = Url1 % page #url 合成
    #获得ID,用来去文章所在网站
    idListPage = getPage(Url)#获得 article目录 html文件内容
    soupA= BeautifulSoup(idListPage,'lxml') #解析html(???)
    List = soupA.find_all(attrs='article block untagged mb15')#生成一个list,
    for string in List:#遍历
        idInfo = string.get('id')#获取各个string里面的{id = '...'}
        idInfo1 = str(idInfo)#信息字符串化
        articleId = idInfo1.strip()[11:]#截取idnumber
        #articleId = str(string.get('id')).strip()[11:]
        idList.append(articleId#获得Id列表

for Id in idList:
    furl = comUrl % Id#合成文章页面地址
    artCont = getPage(furl)#获得html
    soupB=BeautifulSoup(artCont,'lxml')#解析
    mainContent = soupB.find(id='single-next-link')#筛选第一次,把内容快圈出来 , html
    mainText = mainContent.find(class_ ='content').get_text()#截取正文内容
    articleFloor += 1
    print articleFloor,mainText

     ####尝试打印图片失败,因为找不到截取imgurl 的方法
    try:
        imgUrl1= mainContent.find()
    except:
        pass
    #打印神评论
    try:
        sp = soupB.find(class_='main-text').get_text()#找到神评块
        print '    ',sp
    except:
        print 'no sp'





###Note:
''' 1.response status_code -> evernote http/1.1

    2.try ,except 功能测试成功再加上去

    3.BeautifulSoup->find_all(findAll)
        .find()
        .findAll()
        class_=...

        属性查找print soup.find_all("a", attrs={"class": "sister"})



###question:
    1.q = Soup1.find_all('a')
        q是什么格式?  list

###disadvantage of the programme:
    id list have to take a long time to be wholely get
    which means programmer have can not see the outcome quickly.



'''
