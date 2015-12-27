# -*- coding: utf-8 -*-
'''
Created on 2015年12月27日

@author: WJLUCK
'''

class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = []  #list用来存放收集到的全部数据，每个元素是个dict结构。
    
    def collect_data(self, data): #用于收集数据
        if data is None or data == {}:
            return 
        self.datas.append(data)

    
    def output_html(self):  #用于将收集好的数据写出到一个html文件中。对象自身维护一个list表。
        fout = open('result.html','w')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['title'].encode('utf-8'))
            fout.write('<td>%s</td>' % data['summary'].encode('utf-8'))
            fout.write('</tr>')        
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()
        
        


    
    
    



