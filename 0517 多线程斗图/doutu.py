# -*- coding:utf-8 -*-
import requests, threading
from lxml import etree
from bs4 import BeautifulSoup

#获取源码
def get_html(url):#获得网页文件
    #url = 'https://www.doutula.com/article/list/?page={}'.format(a)
    userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    headers = {'User-Agent':userAgent}
    req = requests.get(url= url, headers=headers)#伪装完后的请求
    response= req.content
    #print response
    return response
#get_html()

#匹配图片
def get_img_html(html):
    soup= BeautifulSoup(html,'html.parser')
    all_a = soup.find_all('a',class_= 'list-group-item')#_用于区分,#找到a标签
    #print all_a
    for k in all_a:
        img_html = get_html(k['href'])#获取源码
        #print img_html
        get_img(img_html)

#图片url
def get_img(html):
    soup =etree.HTML(html)#初始化源码
    items = soup.xpath('//div[@class="artile_des"]')#//匹配标签[(@名称)条件=(是)什么]
    for item in items:
        imgurl_list = item.xpath('table/tbody/tr/td/a/img/@onerror')
        #print imgurl_list
        start_save_img(imgurl_list)

#多线程实现

def start_save_img(imgurl_list):
    for k,i in enumerate(imgurl_list):

        #可调用对象, args调用吃的那列表
        th =threading.Thread(target = save_img,args=(i,))
        th.start()
'''
def start_save_img(list):
    for i in list:
        th = thread.start_new_thread(save_img, (i,))
        '''


#下载图片
x=0
def save_img(img_url):
    global x
    x+=1
    a=x
    img_url = img_url.split('=')[-1][1:-2].replace('jp','jpg')
    tpurl='http:'+ img_url
    print str(a)+'    '+tpurl

    img_content= requests.get(tpurl).content
    with open('doutu/%d.jpg'%a,'w+') as f:
        f.write(img_content)



#if __name__== '__main__':
#    main()
#以上:主函数另一种表达
#主函数

def main():
    start_url = 'https://www.doutula.com/article/list/?page={}'
    for v in range(1,10):
        start_html = get_html(start_url.format(v))#字符串格式化,获取源码;format()==%d%page
        get_img_html(start_html)#获取页内图片

if __name__ =='__main__':
    main()

'''
###
1.'....{}'.format

2. items = soup.xpath('//div[@class="artile_des"]')
    #//匹配标签[(@名称)条件=(是)什么]
    30



'''
