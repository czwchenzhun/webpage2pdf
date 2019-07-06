#！-*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from multiprocessing import Process,Queue

class WebRender(QWebEngineView):
    def __init__(self,queWait,queFinish):
        super().__init__()
        self.queWait=queWait
        self.queFinish=queFinish
        self.page=self.page()
        self.url=None
        self.html=None
        self.savePath=None
        self.running=False      #纪录当前是否在运行
        self.signalConnect()

    #from url (example:"http://www.baidu.com/")
    def from_url(self,url,savePath):
        self.url=url
        self.savePath=savePath
        self.load(QUrl(url))

    #from html text
    def from_html(self,html,savePath):
        self.html=html
        self.savePath=savePath
        self.setHtml(html)

    #from local html file
    def from_localFile(self,url,savePath):
        self.url='file:///'+url
        self.savePath=savePath
        self.load(QUrl(self.url))

    def signalConnect(self):
        self.loadFinished.connect(self.onLoadFinished)
        self.page.pdfPrintingFinished.connect(self.onPdfPrintingFinished)

    def onLoadFinished(self):
        self.page.printToPdf(self.savePath)

    def onPdfPrintingFinished(self,savePath,success):
        self.queFinish.put(savePath+','+str(success))
        self.running=False
        self.run()

    def dispatchTask(self,taskDes):
        _type,arg1,arg2=taskDes.split(',')
        if _type=='url':
            self.from_url(arg1,arg2)
        elif _type=='html':
            self.from_html(arg1,arg2)
        elif _type=='file':
            self.from_localFile(arg1,arg2)
        elif _type=='close':
            self.close()
        self.running=True

    def run(self):                                      #启动第一个任务，触发任务链
            taskDes=self.queWait.get(True)  #取得描述任务的字符串
            self.dispatchTask(taskDes)


def createRender(queWait,queFinish,showUI=False):
    app=QApplication(sys.argv)
    webRender=WebRender(queWait,queFinish)
    if showUI:
        webRender.show()
    webRender.run()
    sys.exit(app.exec_())


class RenderManager:
    def __init__(self):
        self.queWait=Queue()        #存放用于描述等待被执行的任务的字符串
        self.queFinish=Queue()      #存放用于描述执行完毕的任务的字符串
        self.processList=[]             #存放创建的所有进程
        self.taskNum=0

    def addRender(self,num=1,showUI=False):
        for i in range(num):
            process=Process(target=createRender,args=(self.queWait,self.queFinish,showUI,))
            process.start()
            self.processList.append(process)

    def from_url(self,url,savePath):
        self.queWait.put('url,'+url+','+savePath)
        self.taskNum+=1

    def from_html(self,html,savePath):
        self.queWait.put('html,'+html+','+savePath)
        self.taskNum+=1

    def from_localFile(self,filePath,savePath):
        if '\\' in filePath:
            filePath=filePath.replace('\\','/')
        self.queWait.put('file,'+filePath+','+savePath)
        self.taskNum+=1

    #终结num个数目的进程，num默认为1
    def terminate(self,num=1):
        for i in range(num):
            self.queWait.put('close,_,_')

    #终结所有进程
    def terminateAll(self):
        for process in self.processList:
            process.terminate()

    def waitFinish(self):
        while self.taskNum>0:
            des=self.queFinish.get(True)
            print(des)
            self.taskNum-=1
        self.terminateAll()
