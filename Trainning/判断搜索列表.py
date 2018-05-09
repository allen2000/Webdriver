# -*- coding: UTF-8 -*-
import time
import os
import xlrd
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from xlutils.copy import copy
from openpyxl import load_workbook
from openpyxl import Workbook

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)
driver.get('http://www.baidu.com')
driver.find_element_by_id("kw").send_keys("Selenium")
driver.find_element_by_id("su").click()

time.sleep(2)
# 第二个判断方法
ele_string = driver.find_element_by_xpath("//div/h3/a[text()='官网']/../a").text
if (ele_string == u"Selenium - Web Browser Automation"):
    print "测试成功，结果和预期结果匹配！"
driver.quit()
#----------------------------------------------------------------------------------------------
#第一种判断
time.sleep(2)
# 这里通过元素XPath表达式来确定该元素显示在结果列表，从而判断Selenium官网这个链接显示在结果列表。
# 这里采用了相对元素定位方法/../
# 通过selenium方法is_displayed() 来判断我们的目标元素是否在页面显示。
#driver.find_element_by_xpath("//div/h3/a[text()='官网']/../a/em[text()='Selenium']").is_displayed()
#driver.quit()

