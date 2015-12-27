# -*- coding: utf-8 -*-
'''
Created on 2015年12月27日

@author: WJLUCK
'''


class UrlManager(object):
    
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
    
    def add_new_url(self, url):
        if url == None:             #if url is None:    也可以这样写？？和我这样有何区别？
            return 
        if url in self.old_urls:    #if url not in self.new_urls and url not in self.old_urls: not in 已经这种连写逻辑式
            return 
        self.new_urls.add(url)            
    
    #这里传进来的urls是的集合set()
    def add_new_urls(self, urls):   
        if urls == None:            #if urls is None or len(urls) == 0
            return 
        for url in urls:                 #需不需要考虑传进来的urls是个什么类型？？？写这个模块的时候就要想到传进来的urls是个set吧。 
            self.add_new_url(url)        #如何调用自己类中的方法，self这样引用已经定义好的方法可以吧？??可以。
        
    
    def has_new_url(self):
        return len(self.new_urls) != 0

    
    def get_new_url(self):
        url = self.new_urls.pop()
        self.old_urls.add(url)
        return url

    
