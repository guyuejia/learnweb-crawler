# -*- coding: utf-8 -*-
'''
@File    :   test.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/8/5 22:15   gujiayue      1.0         None
'''

from selenium import webdriver
import time
browser = webdriver.Chrome(r"D:\OneDrive\Programe Projects\Python\browserDriver\chromedriver.exe")
browser.get("http://www.nmc.cn/publish/observations/hourly-precipitation.html")
html = browser.execute_script("return document.documentElement.outerHTML")
print(html)

