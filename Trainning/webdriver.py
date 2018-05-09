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
driver.get('http://www.baidu.com/')

driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()
time.sleep(1)
driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
time.sleep(1)
driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
# 断言方法一
error_mes = driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__error"]').text
try:
    assert error_mes == u'请您输入手机/邮箱/用户名'
    print ('Test pass.')
except Exception as e:
    print ("Test fail.", format(e))