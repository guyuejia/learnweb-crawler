from selenium import webdriver
option = webdriver.ChromeOptions()
#浏览器页面隐藏不展示
option.add_argument('headless')
browser = webdriver.Chrome("D:\\test\\chromedriver.exe",options=option)

browser.get("C:\\Users\\HU\PycharmProjects\\learnweb-crawler\\resource\\example.html")
