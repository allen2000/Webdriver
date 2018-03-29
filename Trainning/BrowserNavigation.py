# -*- coding: UTF-8 -*-
from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
print "Base URL:",driver.current_url
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
print "After search URL:",driver.current_url

driver.back()
print "Back URL:",driver.current_url

driver.forward()  # forward
print 'forward to: ', driver.current_url

time.sleep(2)
driver.refresh()  # refresh
print 'refresh: ', driver.current_url