"""
隐式等待：implicitly_wait的使用，此种等待只适用于查找元素的时候，不适用加载网页的等待时间
当使用了隐士等待执行测试的时候，如果 WebDriver没有在 DOM中找到元素，将继续等待，超出设定时间后则抛出找不到元素的异常
换句话说，当查找元素或元素并没有立即出现的时候，隐式等待将等待一段时间再查找 DOM，默认的时间是0
一旦设置了隐式等待，则它存在整个 WebDriver 对象实例的声明周期中，隐式的等到会让一个正常响应的应用的测试变慢，
它将会在寻找每个元素的时候都进行等待，这样会增加整个测试执行的时间。
"""
from selenium import webdriver
browser = webdriver.Chrome("../browserdriver/chromedriver.exe")

#设置隐式等待时间,该设置全局有效。
browser.implicitly_wait(10)

browser.get("https://www.baidu.com")
#从网页上找一个根本不存在的id,代码不会立即返回错误，而是等待10s后才报错
browser.find_element_by_id("test")
#找一个存在的id，立即完成，不会等待
browser.find_element_by_id("kw")

#把隐式等待时间设置为0
browser.implicitly_wait(0)
#从网页上找一个根本不存在的id,代码立即返回错误
browser.find_element_by_id("test")