# -*- coding: utf-8 -*-
'''
Created on 2015年12月27日

@author: WJLUCK
'''
from baike_spider import url_manager, html_downloader, html_parser,\
    html_outputer



#为什么要把这个爬虫类创建在这里？创建在一个新的模块中会更好吧？
#这个爬虫总调度程序会使用url管理器，html下载器和解析器，输出器四个对象来完成所需要的功能。一种管理器被定义成了一个对象。面向对象编程。
#用到的这些模块中的对象会在该爬虫的构造函数中初始化。
class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()        #先把要用到的模块中的类定义好，再在下面写类中的具体方法。
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()    
        
    
    #爬虫的调度程序,传入一个种子url以及需要爬取的网页的数量。
    def craw(self, root_url, number):        
        count = 1
        self.urls.add_new_url(root_url)                 
       
        #启动爬虫的循环
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()               #这里使用到了类中的具体方法，先把要用到的方法名写好，之后再去写具体的实现方法。
                print 'craw %d : %s' %(count, new_url)
                
                #这里的变量存放的是什么格式的变量   ？？？不需要考虑吗？？       html_cont = urllib2.urlopen(url).read()
                html_cont = self.downloader.download(new_url)  
                
                #直接将上一步返回的html_cont 传入下面这个函数就能解析？？       soup = BeautifulSoup(html_cont, 'html.parser', from_encoding = 'utf-8')  
                new_urls, new_data = self.parser.parse(new_url, html_cont)  
                
                
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)    #这里是先将数据完全收集到一个字典中，之后整体进行写文件。也可以边爬边写，更好一点吧。       
                if count == number:                     #这里的number是我们需要爬取的网页的总数目。
                    break
                count = count + 1   
            except:
                print 'craw failed'                     #这里非常好，同时处理了多个异常，只要出现了问题就不爬取这个网页。打印失败，并且还没有count+1            
        self.outputer.output_html()                     #整体写文件。


#main函数的作用就是给爬虫一个种子url并且启动爬虫。
if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    print '爬虫开始工作'
    obj_spider.craw(root_url, 1) 
    print '爬取结束'
