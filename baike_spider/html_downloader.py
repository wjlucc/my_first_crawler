# -*- coding: utf-8 -*-
'''
Created on 2015年12月27日

@author: WJLUCK
'''
import urllib2


class HtmlDownloader(object):
    
    
    def download(self, url):
        if url is None:
            return None                 #这里的return None 和 return 是相同的
        response = urllib2.urlopen(url)
        
        if response.getcode() == 200:   
            return response.read()      #这里返回去的是个什么类型的变量？？？不关心类型，只要另一个parser能够解析就行？？？什么时候考虑这点？
        else:
            return None
            
    