# -*- encoding: UTF-8 -*-

import re, urllib2
from bs4 import BeautifulSoup

files = open('quick.html','w+')

urls = {21087:0}
count = 0

while(True):
    if count > 5:
        break
    
    for k in urls:
        if urls[k] == 0:
            newcont = ''
            url = 'http://baike.baidu.com/view/'+ str(k) +'.htm'
            response = urllib2.urlopen(url)
            cont = response.read()
            
            soup = BeautifulSoup(cont,'html.parser','utf8')
            
            newcont = str(soup.find('dd'))
            newcont = newcont + str(soup.find('div',class_='lemma-summary'))
            files.write(newcont)   
            print newcont  
            
            s = soup.find_all(href = re.compile(r'/view/\d+\.htm')) #s是不是一个list？
            for i in s:
                s = str(i)
                ss = re.split('[/.]',s)
                if ss[2] in urls:
                    pass
                else:
                    urls[ss[2]] = 0     #迭代过程中是否可以添加元素。
                
            urls[k] = 1     #迭代的过程中，能不能向集合中添加元素及值？
            count = count + 1
            break
        else:
            continue
files.close()







