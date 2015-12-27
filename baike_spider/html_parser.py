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
        links = soup.find_all('a', href = re.compile(r'/view/\d+\.htm'))    #这里的links是什么类型的变量？？直接可以迭代？每一个元素是一个字典？
        for link in links:      #这里的link是一个字典？？
            new_url = link['href']  #这个字典中还有别的元素？
            new_full_url = urlparse.urljoin(page_url, new_url)  #page_url 是在这里被用到的。这个方法是根据基类改造url。
            urls.add(new_full_url)
        return urls
            
            
            
    def _get_new_data(self, page_url, soup):
        res_data = {}
        res_data['url'] =page_url       #这里用到了原始url
        
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1></dd>
        title_node = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')  #两次find最终能得到标题的标签。
        res_data['title'] = title_node.get_text()
        
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find("div", class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()
        
        return res_data 
    
    
    
    #这个函数最后返回的是urls和data，url是个字典。
    def parse(self, page_url, html_cont):   #这里的html_cont是通过上一步的response.read()返回来的变量，不用关心变量类型，直接使用？？？
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding = 'utf-8')
        new_urls = self._get_new_urls(page_url, soup)   #传入的参数为什么需要page_url？内部使用的方法也是先使用方法，再声明方法，最后再去定义。
        new_data = self._get_new_data(page_url, soup)   #这里为何也需要两个参数？直接根据解析的内容也能获得数据呀？？？
        return new_urls, new_data   #最终的urls以set()形式返回，data以字典形式返回去
        
        
    
    



