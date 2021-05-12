# -*- coding: utf-8 -*-
'''
@File    :   selectBox.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/12/30 14:54   gujiayue      1.0         处理网页中下拉框的
'''
#方法1：直接定位到下拉框进行选择。一般适用于下拉框的标签名称就是select，selenium给了有力的支持，就是Select类
#详细参考：https://www.cnblogs.com/z-x-y/p/9020833.html。


import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driverPath = r"D:\OneDrive\Programe Projects\Python\browserDriver\chromedriver.exe"
driver = webdriver.Chrome(driverPath)
driver.get('http://sahitest.com/demo/selectTest.htm')

s1 = Select(driver.find_element_by_id('s1Id'))  # 实例化Select

s1.select_by_index(1)  # 选择第二项选项：o1
time.sleep(10)
s1.select_by_value("o2")  # 选择value="o2"的项
s1.select_by_visible_text("o3")  # 选择text="o3"的值，即在下拉时我们可以看到的文本
driver.quit()

#方法2：针对下拉框的标签名称是input
#针对该种类型的处理，首先定位到该下拉input元素，然后鼠标点击，这时候就把下拉框选项都展示出来了
#然后，定位到要选择的选项元素，再次click，就完成了选择