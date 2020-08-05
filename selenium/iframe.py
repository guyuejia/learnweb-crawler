# -*- coding: utf-8 -*-
'''
@File    :   iframe.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/8/1 17:32   gujiayue      1.0         处理iframe的方法
'''

from selenium import webdriver
import time
browser = webdriver.Chrome(r"D:\OneDrive\Programe Projects\Python\browserDriver\chromedriver.exe")
#该网址下的详细预警信息内容其实是在一个iframe里面，需要先定位到iframe，然后再处理
browser.get("http://he.cma.gov.cn/qxfw/yjxx/")
time.sleep(5)

#方法1，先找出该页面的所有ifram元素,通过tag
iframes = browser.find_elements_by_tag_name("iframe")
#上一步能找到2个iframe，我们实际要定位的是第二个，所以可以通过索引切换到该ifarme，然后swtich到该元素，剩下的操作就是在该iframe里面了
browser.switch_to.frame(iframes[1])

warningTables = browser.find_element_by_id("warning_table")
warningList = warningTables.find_elements_by_xpath("//div[@class='warning_list']")

print("共计预警信息条目是：{}".format(len(warningList)))

#可以通过该语句返回到主页面
browser.switch_to.default_content()

browser.close()

#方法2，直接通过索引进行切换，switch的参数如果是整形就会认定是索引
# browser.switch_to.frame(1)

#方法3，如果iframe有id或者name的话也可以通过id或者name，直接switch就可以。参数如果是字符串就会认定是id或者name
# browser.switch_to.frame("name or id")

