"""
判断页面某个元素是否存在的方法
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#方法一：直接判断,不建议用
def is_element_present(browser,by, value):
    try:
        element = browser.find_element(by=by, value=value)
    except NoSuchElementException as e:
        return False
    return True

#方法二：使用延时等待检查元素是否存在,默认等待5s
def is_element_exist(browser,locator,delay=5):
    wait = WebDriverWait(browser, delay)
    try:
        wait.until(EC.visibility_of_element_located(locator))
    except TimeoutException:
        return False
    return True

if __name__ == '__main__':

    driverPath = r"../browserdriver/chromedriver"
    print(driverPath)
    browser = webdriver.Chrome(driverPath)
    browser.get("https:///www.baidu.com")
    searchBox = browser.find_element_by_id("kw")
    locator = (By.ID,"kw")
    print(is_element_exist(browser,locator))
