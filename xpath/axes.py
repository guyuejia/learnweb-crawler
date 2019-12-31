"""
xpath中轴的用法实例
"""
from selenium import webdriver
browser = webdriver.Chrome("D:\\test\\chromedriver.exe")
browser.get("C:\\Users\\HU\PycharmProjects\\learnweb-crawler\\resource\\example1.html")

#父节点定位子节点
print("----------父节点定位子节点-----------")
#定位B节点的子节点，由于该节点没有id，不能直接通过id定位
#方法1：串联寻找，通过id找到B，在接着根据tag找到该节点
print(browser.find_element_by_id('B').find_element_by_tag_name('div').text)
#方法2：xpath父子关系寻找
print(browser.find_element_by_xpath("//div[@id='B']/div").text)
#方法3：xpath轴 child，通过child定位出第二个div子节点
print(browser.find_element_by_xpath("//div[@id='B']/child::div[2]").text)

#子节点定位父节点
#通过子节点C，定位其两级父节点div
print("----------子节点定位父节点-----------")
#方法1：..代表了上一级节点
print(browser.find_element_by_xpath("//div[@id='C']/../..").text)
#方法2：xpath轴，parent代表了获取上一级父节点
print(browser.find_element_by_xpath("//div[@id='C']/parent::*/parent::div").text)

#弟弟节点定位哥哥节点
#通过节点D，定位哥哥节点，brother1
print("----------弟弟节点定位哥哥节点-----------")
#方法1：简单直接的方法，先找到父节点，再找哥哥
print(browser.find_element_by_xpath("//div[@id='D']/../div[1]").text)
#方法2：xpath轴,preceding-sibling，其能够获取当前节点的所有同级哥哥节点，
#注意括号里的标号，1 代表着离当前节点最近的一个哥哥节点，数字越大表示离当前节点越远
print(browser.find_element_by_xpath("//div[@id='D']/preceding-sibling::div[1]").text)

#哥哥节点定位弟弟节点
#通过节点D，定位弟弟节点，brother2
print("----------哥哥节点定位弟弟节点-----------")
#方法1：xpath，通过父节点获取其弟弟节点
print(browser.find_element_by_xpath("//div[@id='D']/../div[3]").text)
#方法2：xpath轴，following-sibling
print(browser.find_element_by_xpath("//div[@id='D']/following-sibling::div[1]").text)
#方法3：xpath轴，following
print(browser.find_element_by_xpath("//div[@id='D']/following::*").text)

browser.quit()