import selenium
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://market.m.taobao.com/app/local-life/commercial-tts/index.html#/home')
driver.maximize_window()

driver.implicitly_wait(10)
driver.find_element_by_xpath('//button[@class="ant-btn ant-btn-primary"]').click()
old_win = driver.current_window_handle
wins = driver.window_handles
driver.switch_to.window(wins[-1])
driver.find_element_by_xpath('//li[@data-status="show_login"]').click()

driver.find_element_by_id("J-input-user").send_keys('kbtestyufabu21@alipay.com')
driver.find_element_by_id("password_rsainput").send_keys('koubei21')
driver.find_element_by_xpath('//input[@type="submit"]').click()
time.sleep(10)
driver.switch_to.window(old_win)

try:
    b = driver.find_element_by_xpath("//div[contains(text(),'kfc')]").location_once_scrolled_into_view
except:
    pass
else:
    driver.find_element_by_xpath('(//a[@class="mr8"])[13]').click()

# driver.quit()
#sssss
