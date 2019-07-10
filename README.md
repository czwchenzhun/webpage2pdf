<a>This is a simple wrapper of the QWebEngineView(PyQt5) class.</a><br>
<a>It's base on the client/server model.</a>
<h3>Requirements</h3>
<ul>
	<li>python3</li>
	<li>PyQt5</li>
</ul>
<p style="color: #006dad;">Errors will occur if the version of PyQt5 is too high.Cause <strong>PyQt5.QtWebEngineWidgets</strong> not exist.</p>
<div style="background-color:#f9f9f9;border:2px solid #d3d3d3;">
	<pre>	pip install PyQt5==5.10.1</pre>
</div>
<h3>Usage</h3>
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
		#rm.from_localFile('html/test.html','2.pdf')
		print('start.')
		rm.waitFinish()
		print('finish all.')		
	</pre>
</div>