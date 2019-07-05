#！-*- coding:utf-8 -*-
from webpage2pdf import RenderManager
import time

if __name__=='__main__':
    rm=RenderManager()
    rm.addRender(1,showUI=True)
    rm.from_url('http://www.hao123.com','0.pdf')
    rm.from_html("<a>Hello World!你好世界！</a>",'1.pdf')
    #rm.from_localFile(r'Test.html','2.pdf')
    time.sleep(5)
    print('start')
    #taskNum用于记录任务的总数,自动增长
    #从记录已经完成的任务的队列中取出，任务执行结果的描述信息
    #取得一条记录代表着完成一个任务，taskNum -1，taskNum为0时代表全部执行完成
    #terminateAll终结所有进程
    #也可以调用terminate(num)来决定结束多少个进程
    while rm.taskNum>0:
        des=rm.queFinish.get(True)
        print(des)
        rm.taskNum-=1
    rm.terminateAll()
    print('finish all')
