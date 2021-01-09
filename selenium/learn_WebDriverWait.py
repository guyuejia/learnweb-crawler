"""
默认get方法是必须等待加载完才会执行后续的代码，这样的话其实导致了显示等待和隐式等待的方法都是不生效的
可以通过设置get直接返回，不再等待界面加载完成。然后再通过显示或者隐式的方法等待
"""
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#默认get方法是必须等待加载完才会执行后续的代码
# 通过设置get直接返回，不再等待界面加载完成，该设置必须在初始化浏览器之前完成
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["pageLoadStrategy"] = "none"

#注意，一定要chrome浏览器的版本和驱动程序的版本要对应，否则就会出现异常
browser = webdriver.Chrome("../browserdriver/chromedriver.exe")
#隐式设定最大等待查找某个元素的时间，这个设置是针对browser的，全局有效
#browser.implicitly_wait(10)

"""
WebDriverWait()会配合until()和until_not()方法一起使用，
根据判断条件而进行灵活进行处理时间等待问题，他会不断的根据你设定的条件去判断，直到超过你设置的等待时间，
如果设置的条件满足，然后进行下一步操作，
如果没有满足会报一个'selenium.common.exceptions.TimeoutException: Message: '错误，
"""
webDriverWait = WebDriverWait(browser,10)
browser.get("https://movie.douban.com/subject/26266893/")

path = "//*[@id='content']/h1/span[1]"

#通过显示的方法，until 也属于WebDriverWait,代表一直等待,直到某元素可见，until_not与其相反，判断某个元素直到不存在
try:
    print("开始查询：",datetime.now())
    webDriverWait.until(EC.presence_of_all_elements_located((By.XPATH,path)))
    print("第一个元素查找完成：",datetime.now())
    #试着找一个不存在的元素
    webDriverWait.until(EC.presence_of_all_elements_located((By.ID, "TEST")))
    print("第二个元素查找完成：", datetime.now())

except TimeoutException as e:
    print("显示等待超时，没有查到该元素",datetime.now())
finally:
    movieName=browser.find_element_by_xpath(path)
    print(movieName.text)
    print("查询结束",datetime.now())

browser.quit()