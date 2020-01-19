from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import time


driver = webdriver.Chrome()     # 创建Chrome对象.
# 操作这个对象.
#driver.get('http://www.baidu.com')    
#driver.get('https://mail.zjut.edu.cn/?q=login&code=1')    
#driver.get('https://www.taobao.com/')    
#print(driver.find_element_by_link_text('新闻').text)
#driver.find_element_by_id("submit").click()
driver.maximize_window()
#driver.find_element_by_xpath('//*[@id="J_SiteNavMytaobao"]/div[1]/a').click()
#time.sleep(5)
driver.get('https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/')    
driver.find_element_by_xpath('//*[@id="J_QRCodeLogin"]/div[5]/a[1]').click()
#print(driver.title)
elemm=driver.find_element_by_id('TPL_username_1')
elemm.send_keys('空星邃深')
elemm2=driver.find_element_by_id('TPL_password_1')
elemm2.send_keys('33dsdf')
driver.save_screenshot(r'C:\Users\哈哈哈\Desktop\avb.png')
elemm3=driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')
width3=elemm3.size['width']
loc=elemm3.location['x']
print(elemm3.size['height'])
print(elemm3.size['width'])
elemm4=driver.find_element_by_xpath('//*[@id="nc_1__scale_text"]/span')
width4=elemm4.size['width']
print(elemm3.location)
print(elemm4.location)
print(elemm4.size['height'])
print(elemm4.size['width'])
x_location=loc+width4
y_location=elemm4.location['y']
ActionChains(driver).drag_and_drop_by_offset(elemm3, x_location, y_location).perform()

#ActionChain(driver).drag_and_drop_by_offset(elemm3,``)
time.sleep(20)
driver.quit()
