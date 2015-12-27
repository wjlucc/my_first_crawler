# -*- encoding:utf8 -*-

'''
Created on 2015年12月27日

@author: WJLUCK
'''
from baike_crawler import url_manager, html_outer, html_parser
url = 'http://baike.baidu.com/view/21087.htm'
count = 0



url_manager = UrlManager()
html_outer = HtmlOuter()




while count < 10:    
        
    urls,data = html_parser.parser(url)
    
    url_manager.add_urls(urls)
    
    html_outer.out(url,data)
    
    url = url_manager.get_url()
    
    count = count + 1








