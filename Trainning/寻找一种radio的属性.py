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
driver.get('http://news.baidu.com/')

for i in driver.find_elements_by_xpath("//*/input[@type='radio']"):
    print i.get_attribute('value')