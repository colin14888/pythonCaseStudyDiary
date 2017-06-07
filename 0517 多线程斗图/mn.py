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

#获得看图页面menuUrl,找到mnurl
def getMnUrl(Url):
    cont=get_html(Url)

    soup1= BeautifulSoup(cont,'lxml')
    menuPack = soup1.find(class_='lanmu_pic3')
    list = menuPack.find_all('p')
    for i in list:
        li=i.find('a')
        page = li.get('href')
        ID = str(page).strip()[-8:-4]
        getPage(ID)

def getPage(ID):
    first(ID)
    mnPage = 'http://www.juekong.com/meinv/{}_2.htm'.format(ID)
    soup2= BeautifulSoup(get_html(mnPage),'lxml')
    #总页数
    pageN = soup2.find('h1')
    pageN = re.split('/',str(pageN))[1]
    pageN = re.split('\)',pageN)[0]
    startSavePic(pageN,ID)

def first(ID):
    url='http://www.juekong.com/meinv/{}.htm'.format(ID)
    soup3=BeautifulSoup(get_html(url),'lxml')
    imgUrl = soup3.find(class_='IMG_show')
    imgUrl = imgUrl.get('src')
    get(imgUrl,1,ID)


def startSavePic(n,ID):
    for k,i in enumerate(range(2,int(n))):
        try:
            th = threading.Thread(target=savePic,args=(i,ID))
            th.start()
        except Exception,e:
            print 'problem in ',k

def savePic(i,ID):
    url = 'http://www.juekong.com/meinv/%s_%s.htm'%(ID,i)
    soup3=BeautifulSoup(get_html(url),'lxml')
    imgUrl = soup3.find(class_='IMG_show')
    imgUrl = imgUrl.get('src')
    get(imgUrl,i,ID)

def get(src,i,ID):
    img_content = requests.get(src).content
    print i,ID
    with open('mn/%s-%s.jpg'%(ID,i),'wb+') as f :
        f.write(img_content)


#ji获得图片url


#多线程
def download():
    pass


def main():
    url ='http://www.juekong.com/meinv/index{}.html'
    pagee= int(input('要几多页啊?\n呗个整数我之后gum回车'))+1
    for page in range(3,pagee):
        print page
        if page ==1:
            Url = url.format('')
        else:
            Url = url.format('_'+str(page))
        getMnUrl(Url)
if __name__ =='__main__':
    main()
