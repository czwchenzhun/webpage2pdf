#webpage2pdf

<pre>
This is a simple wrapper of the QWebEngineView(PyQt5) class.
It's base on the client/server model.
</pre>
<h1>Usage</h1>
<div style="background-color:#f9f9f9;border:2px solid #d3d3d3;">
	<pre>
		#! -*- coding:utf-8 -*-
		from webpage2pdf import RenderManager		
		#must start from __main__
		if __name__=='__main__':
			rm=RenderManager()
			rm.addRender(num=2,showUI=True)
			rm.from_url('http://www.baidu.com/','0.pdf')
			rm.from_html("<a>Hello World!</a>",'1.pdf')
			#rm.from_localFile('html/test.html','3.pdf')
			print('start.')
			rm.waitFinish()
			print('finish all.')		
	</pre>
</div>