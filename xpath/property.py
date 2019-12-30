"""
在通过路径获取元素的基础上，进一步通过属性来获取更准确的元素
"""
from selenium import webdriver
browser = webdriver.Chrome("D:\\test\\chromedriver.exe")
browser.get("C:\\Users\\HU\PycharmProjects\\learnweb-crawler\\resource\\example.html")

#选取所有包括lang属性的title节点
browser.find_elements_by_xpath("//title[@lang]")
#选取所有包括lang属性,并且属性值为eng的title节点
browser.find_elements_by_xpath("//title[@lang='eng']")

#选取book元素，并且其price元素的值大于35,结果是只有1个元素。
browser.find_elements_by_xpath("//book[price>35]")
#选取book元素的title元素，并且price 元素的值须大于 35.00。
browser.find_elements_by_xpath("/bookstore/book[price>35.00]/title")

#利用通配符，选取所有带有属性的title元素
browser.find_elements_by_xpath("//title[@*]")