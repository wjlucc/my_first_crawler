# -*- coding: utf-8 -*-
'''
Created on 2015年12月27日

@author: WJLUCK
'''

#为什么要把这个爬虫类创建在这里？创建在一个新的模块中会更好？
#这个爬虫总调度程序会使用url管理器，html下载器何解析器
class SpiderMain(object):
    
    
    def craw(self, root_url):
        pass
    
    



if __name__ == "main":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)



