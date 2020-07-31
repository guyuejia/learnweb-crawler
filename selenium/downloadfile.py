# -*- coding: utf-8 -*-
'''
@File    :   downloadfile.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/31 14:47   gujiayue      1.0         下载链接文件
'''
"""
下载链接里的文件到指定目录
"""

from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
#指定下载的目录，如果不存在将创建
prefs = {"download.default_directory": "d:\\iDownload"}
chromeOptions.add_experimental_option("prefs", prefs)

browser = webdriver.Chrome(r"D:\OneDrive\Programe Projects\Python\browserDriver\chromedriver.exe",
                           options = chromeOptions)
browser.get("http://www.ceic.ac.cn/speedsearch?time=1")
file = browser.find_element_by_id("save")
#点击链接后，下载的文件到存放到指定目录里
file.click()
