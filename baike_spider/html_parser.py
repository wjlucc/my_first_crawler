# -*- coding: utf-8 -*-
'''
Created on 2015年12月27日

@author: WJLUCK
'''
import re

from bs4 import BeautifulSoup
import urlparse


class HtmlParser(object):
    
    def _get_new_urls(self, page_url, soup):
        urls = set()
        
        #这里的links可能是个list？？    不用关心，只要能迭代就行？？？    
        #可以看出是满足查找条件的标签的集合。是个特有的类型。
        links = soup.find_all('a', href = re.compile(r'/view/\d+\.htm'))    #这里的links是什么类型的变量？？直接可以迭代？每一个元素是一个字典？
        
        #print links
        #print type(links)
        #print len(links)
        
        for link in links:      #这里的link是一个字典？？?  不是吧，是个其自己的类型？？？   表示一个标签。
            #print link
            #print type(link)
            #print len(link)
            
            new_url = link['href']  #这个字典中还有别的元素？  这个操作获取该标签的值。
            new_full_url = urlparse.urljoin(page_url, new_url)  #page_url 是在这里被用到的。这个方法是根据基类改造url。可以手工改造。
            urls.add(new_full_url)
        return urls
            
            
            
    def _get_new_data(self, page_url, soup):
        res_data = {}
        res_data['url'] =page_url       #这里用到了原始url，可以不用这个的。
        
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1></dd>
        title_node = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')  #两次find最终能得到标题的标签。
        title = title_node.get_text()
        res_data['title'] = title
        
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find("div", class_='lemma-summary')        
        summary = summary_node.get_text()
        res_data['summary'] = summary        
        return res_data 
    
    
    
    #这个函数最后返回的是urls和data，url是个字典。
    def parse(self, page_url, html_cont):   #这里的html_cont是通过上一步的response.read()返回来的变量，不用关心变量类型，直接使用？？？
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding = 'utf-8')
        new_urls = self._get_new_urls(page_url, soup)   #内部使用的方法也是先使用方法，再声明方法，最后再去定义。
        new_data = self._get_new_data(page_url, soup)   #这里为何也需要两个参数？直接根据解析的内容也能获得数据呀？？？
        return new_urls, new_data   #最终的urls以set()形式返回，data以字典形式返回去
        