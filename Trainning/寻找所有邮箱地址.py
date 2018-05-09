# -*- coding: UTF-8 -*-
import time
import os
import xlrd
import re
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
driver.get('http://home.baidu.com/contact.html')

# 得到页面源代码
doc = driver.page_source
emails = re.findall(r'[\w]+@[\w\.-]+',doc) # 利用正则，找出 xxx@xxx.xxx 的字段，保存到emails列表
# 循环打印匹配的邮箱
for email in emails:
    print (email)

#在python正则表达式语法中，Python中字符串前面加上 r 表示原生字符串，用\w表示匹配字母数字及下划线。re模块下findall方法返回的是一个匹配子字符串的列表。
