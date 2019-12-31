from selenium import webdriver
option = webdriver.ChromeOptions()
browser = webdriver.Chrome("D:\\test\\chromedriver.exe",options=option)
browser.get("C:\\Users\\HU\PycharmProjects\\learnweb-crawler\\resource\\example.html")

#获取第一本书籍的价格，也就是得到29.99这个值
#首先定位到价格元素，然后利用text把元素的内容展示出来
price = browser.find_element_by_xpath("//book/price").text
#获取第一本书籍的名称，也就是Harry Potter
#不能像获取价格一样，利用text把元素的文本内容展示出来，需要利用get_attribute("textContent")来获取
title = browser.find_element_by_xpath("//title").get_attribute("textContent")