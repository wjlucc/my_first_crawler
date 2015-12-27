#-*- coding: UTF-8 -*-

'''
Created on 2015年12月26日

@author: WJLUCK
'''

import urllib2, re
from bs4 import BeautifulSoup



#这个文件是用来存放下载好的网页
file_object = open('data.html', 'w+')

#用来存放URL，键是对应网址的关键值，据此可以找到对应的网页
class UrlDict(object):
    __url_dict = {21087:0}
    __count = 0  
    #给set中添加url，该url已存在的话就不添加。
    def add_url(self,num):
        if num in UrlDict.__url_dict:
            return False
        UrlDict.__url_dict[num] = 0
        return True
        
    #获取一个url，并且计数。
    def get_url(self):
        for k in UrlDict.__url_dict:
            
            if UrlDict.__url_dict[k] == 0:                
                UrlDict.__url_dict[k] = 1
                UrlDict.__count = UrlDict.__count + 1
                url = 'http://baike.baidu.com/view/'+ str(k) +'.htm'                
                return url
        
    #返回当前已经下载的url的数目   
    def get_count(self):
        return UrlDict.__count



#这个类是用来解析网页的
class PageParse(object):
    def __init__(self,cont,url,encoding):
        self.soup = BeautifulSoup(cont,url,from_encoding = encoding)
    
    def get_title(self):
        node =  self.soup.find('dd',class_="lemmaWgt-lemmaTitle-title")        
        return node
    def get_abstract(self):
        node = self.soup.find('div',class_='lemma-summary')
        return node
    def get_url(self):
        l =  self.soup.find_all(href = re.compile(r'/view/\d+\.htm'))
        newurl = []
        
        for i in l:
            s = str(i)
            ss = re.split('[/.]',s)
            try:
                newurl.append(int(ss[2]))   
                #print newurl    
            except ValueError:
                pass
        return newurl


url_dict = UrlDict()


#这里是用来下载网页的
for i in range(200):
    url = url_dict.get_url()
    print '正在下载第%s个网页,网址:' % (i+1),url    
    response = urllib2.urlopen(url)    
    cont = response.read()    
    page_parse = PageParse(cont,'html.parser','utf8')
    cont = str(page_parse.get_title())
   
  
    newurl = page_parse.get_url()

    for i in newurl:
        url_dict.add_url(i)     
          
    file_object.write(cont)
    cont = str(page_parse.get_abstract())

    
    file_object.write(cont)

         
    
print '下载已完成'  
file_object.close()


        












