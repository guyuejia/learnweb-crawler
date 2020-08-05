# -*- coding: utf-8 -*-
'''
@File    :   scroll.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/8/5 22:55   gujiayue      1.0         页面滚动相关的用法
'''

from selenium import webdriver
browser = webdriver.Chrome(r"D:\OneDrive\Programe Projects\Python\browserDriver\chromedriver.exe")
browser.get("http://www.nmc.cn/publish/observations/hourly-precipitation.html")
#通过js来实现该网页内嵌的一个滚动条的滚动
#由于页面右侧框内的元素，如果页面展示不出来的时候，也不会被爬取到，所以需要控制页面进行滚动展示
#最重要的部分就是找到到内置滚动条所在的div标签的class name ，可以多测试几次
#能够控制滚动条的div可能不应该是滚动条本身，可能是更上一级的包括滚动条的框，多试试就可以了。
"""
元素.scrollTop=xxx  // 纵向滚动到xxx位置，0是最顶端
元素.scrollLeft=xxx  // 横向滚动到xxx位置，0是最左端

document.getElementsByClassName("scroll")[0].scrollHeight // 获取滚动条高度
document.getElementsByClassName("scroll")[0].scrollWidth // 获取横向滚动条宽度
document.getElementsByClassName("scroll")[0].scrollLeft=xxx // 控制横向滚动条位置
"""
js='document.getElementsByClassName("mCustomScrollBox mCS-dark-3 mCSB_vertical mCSB_inside")[0].scrollTop=10000'
browser.execute_script(js)