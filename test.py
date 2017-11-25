from  selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located

driver = webdriver.Firefox()
wait = WebDriverWait(driver,5)
driver.get('http://google.com')
#
# #remote running
# # driver=webdriver.Remote(
# #     desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,
# #     command_executor='http://192.168.0.154:4444/wd/hub'
# #     )
# # driver.get('http://google.com')
# # driver.quit()
#
# driver.find_element_by_id('lst-ib').send_keys('pyton')
# element = driver.find_element_by_name('btnK')
# element.click()
#
# # driver.get('http://duckduckgo.com')
# # element = driver.find_element_by_css_selector('.) #названия классов через точку перечисляем
#
# #Нажать кнопку на 3-м елементе
# el1=driver.find_elements_by_partial_link_text('python')
# el2 = el1[2]
# time.sleep(5)  #обязательное ожидание
# el2.click()
# print(len(el1)) #напечатать кол-во елементов в списке
# print(el1.size)
# from selenium.webdriver.common.keys import Keys
#
# el3 = wait.until(presence_of_all_elements_located((By.PARTIAL_LINK_TEXT,'python')))
# print(len(el3))