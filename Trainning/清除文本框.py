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
driver.get('http://www.baidu.com')

driver.find_element_by_id("kw").send_keys("Selenium")
try:
    driver.find_element_by_id("kw").clear() # <span style="font-family:'Microsoft YaHei';">调用clear()方法去清除</span>
    print ('test pass: clean successful')
except Exception as e:
    print ("Exception found", format(e))
