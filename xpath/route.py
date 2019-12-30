from selenium import webdriver
browser = webdriver.Chrome("D:\\test\\chromedriver.exe")
browser.get("C:\\Users\\HU\\PycharmProjects\\learnweb-crawler\\xpath\\xpath.html")

#原始网页bookstore为根节点，但实际用chrome打开的网页，会自动前面添加两级节点html和body，所以bokkstore不再是根节点

#绝对路径写法：选择html文档对应路径下的bookstore元素
bookstore=browser.find_element_by_xpath("/html/body/bookstore")
#绝对路径写法：选取第一个book元素，注意角标不是从0开始,另外如果不带脚本默认就是指第一个脚本
#/html/body/bookstore/book[1]和/html/body/bookstore/book的一个意思
book1=browser.find_element_by_xpath("/html/body/bookstore/book[1]")

#相对路径写法：获取第一个book元素,不带角标，默认就是第一个，也就是//book和//book[1]是一个意思
book1=browser.find_element_by_xpath("//book")
#相对路径写法：获取第2个book元素
book2=browser.find_element_by_xpath("//book[2]")
#相对路径写法：获取最后一个book元素
booklast=browser.find_element_by_xpath("//book[last()]")
#相对路径写法：获取倒数第二个book元素
bookprelast=browser.find_element_by_xpath("//book[last()-1]")

#组合路径写法：找到所有紧挨着book元素下面的price元素，注意返回结果是list
prices=browser.find_elements_by_xpath("//book/price")

#通配符写法：找到所有bookstore元素的直接子元素。注意是直接子元素，不包括孙元素，len(directons)的结果是2，因为bookstore只有2个book子元素
directSons=browser.find_elements_by_xpath("//bookstore/*")
#通配符写法：找到所有bookstore元素的所有子元素，len(allSons)的结果是6
allSons=browser.find_elements_by_xpath("//bookstore//*")


#统计页面中book元素的数量，注意是elements不是element
num = len(browser.find_elements_by_xpath("//book"))
