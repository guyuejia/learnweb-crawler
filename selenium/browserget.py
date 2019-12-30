"""
加载页面过大的网页，时间过长，但是想要的元素有时候已经出来了，没有必要等到完全加载完
可以通过设置一个超时时长，来避免页面一直加载
"""
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

#注意，一定要chrome浏览器的版本和驱动程序的版本要对应，否则就会出现异常
browser = webdriver.Chrome("D:\\test\\chromedriver.exe")
#设置页面加载和脚本执行超时时间
browser.set_page_load_timeout(20)
browser.set_script_timeout(20)
try:
    browser.get("https://movie.douban.com/subject/26266893/")
except TimeoutException:
    print("加载过慢")
    browser.execute_script('window.stop()')

path="/html/body/div[5]/div[1]/div[2]/p[11]"
#/html/body/div[5]/div[1]/div[2]/p[10]/span/a
actorName=browser.find_element_by_xpath(path)
print(actorName.text)
