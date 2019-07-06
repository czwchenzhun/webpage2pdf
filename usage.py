#！-*- coding:utf-8 -*-
from webpage2pdf import RenderManager

if __name__=='__main__':
    rm=RenderManager()
    rm.addRender(2,showUI=True)
    rm.from_url('http://www.hao123.com','0.pdf')
    rm.from_html("<a>Hello World!你好世界！</a>",'1.pdf')
    rm.from_url('http://www.sougou.com','2.pdf')
    rm.from_url('http://www.bilibili.com','3.pdf')
    rm.from_url('http://www.nowcoder.com','4.pdf')
    rm.from_url('http://www.hao123.com','5.pdf')
    #rm.from_localFile('css/test.html','6.pdf')
    print('start')
    rm.waitFinish() 
    print('finish all')
