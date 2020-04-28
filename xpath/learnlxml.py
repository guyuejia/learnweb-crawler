# -*- coding: utf-8 -*-
'''
@File    :   learnlxml.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/5 21:19   gujiayue      1.0         None
'''

from lxml import html
etree = html.etree
#读取文本解析节点
text='''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">第一个</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0"><a href="link5.html">a属性</a>
     </ul>
 </div>
'''
html=etree.HTML(text) #初始化生成一个XPath解析对象
result=etree.tostring(html,encoding='utf-8')   #解析对象输出代码
print(type(html))
print(type(result))
print(result.decode('utf-8'))

###############################################################################
html=etree.parse("../resource/example1.html",etree.HTMLParser()) #指定解析器HTMLParser会根据文件修复HTML文件中缺失的如声明信息
result=etree.tostring(html)   #解析成字节
#result=etree.tostringlist(html) #解析成列表
print(type(html))
print(type(result))
#这样是能够解析成字符串
print(str(etree.tostring(html, encoding='utf8'), 'utf-8'))
#这样是解析成字节
print(result)
