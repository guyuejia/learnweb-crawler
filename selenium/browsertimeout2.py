"""
默认get方法是必须等待加载完才会执行后续的代码，这样的话其实导致了显示等待和隐式等待的方法都是不生效的
可以通过设置get直接返回，不再等待界面加载完成。然后再通过显示或者隐式的方法等待
"""
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#默认get方法是必须等待加载完才会执行后续的代码
# 通过设置get直接返回，不再等待界面加载完成
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["pageLoadStrategy"] = "none"

#注意，一定要chrome浏览器的版本和驱动程序的版本要对应，否则就会出现异常
browser = webdriver.Chrome(r"D:\OneDrive\Programe Projects\Python\browserDriver\chromedriver.exe")

#隐式设定最大等待查找某个元素的时间，这个设置是针对browser的，全局有效
#browser.implicitly_wait(10)
webDriverWait = WebDriverWait(browser,10)
browser.get("https://movie.douban.com/subject/26266893/")

path = "//*[@id='content']/h1/span[1]"
try:
    print(datetime.now())
    webDriverWait.until(EC.presence_of_all_elements_located((By.XPATH,path)))
#/html/body/div[5]/div[1]/div[2]/p[10]/span/a
finally:
    movieName=browser.find_element_by_xpath(path)
    print(movieName.text)
    print(datetime.now())
