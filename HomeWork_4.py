from selenium import webdriver
import time
# 1,2.
# driver = webdriver.Chrome('c:\\chromedriver.exe')
# driver_2 = webdriver.Firefox(executable_path='c:\\geckodriver.exe')
# driver_2.get('https://www.ynet.co.il')
# driver.get('https://www.walla.co.il/')
# walla_title = driver.title
# print(driver.title)
# driver.refresh()
# if driver.title == walla_title:
#     print('same title as before')
# print(driver.title)
# driver.close()

# 3.yes
# driver_2.get('https://www.google.com')
# print(driver_2.find_element_by_id('hplogo'))
# driver_2.close()
#
# driver.get('https://www.google.com')
# print(driver.find_element_by_id('hplogo'))
# driver.close()
#

# 4.
# driver_2.get('https://translate.google.co.il/?hl=iw&tab=TT#view=home&op=translate&sl=auto&tl=en')
# input_wrap = driver_2.find_element_by_id('source')
# input_wrap.send_keys("שלום")

# 5.
# driver.get('https://www.youtube.com/')
# search = driver.find_element_by_id('search')
# search.send_keys('m.a.a.d city')
# driver.find_element_by_id('search-icon-legacy').click()

# 6. i dont have translate button

# driver.find_element_by_id('search-icon-legacy').click()
# driver.find_element_by_class_name('style-scope ytd-searchbox').click()
# driver.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()

# 7.
# driver.get('https://www.facebook.com/')
# driver.find_element_by_id("email").send_keys('admin1')
# driver.find_element_by_id("pass").send_keys('admin1')
# driver.find_element_by_id('u_0_2').click()

# 8.
# print(driver.get_cookies())
# driver.delete_all_cookies()
# print(driver.get_cookies())

# 9.
# from selenium.webdriver.common.keys import Keys
# driver.get('https://github.com/')
# driver.find_element_by_name('q').send_keys('selenium' + Keys.ENTER)

# 10
# from selenium.webdriver.chrome.options import Options
# disable_all_extensions = Options()
# disable_all_extensions.add_argument('--disable-extensions')
# driver_3 = webdriver.Chrome('c:\\chromedriver.exe', options=disable_all_extensions)
#
# from selenium.webdriver.firefox.options import Options
# disable_all_extensions1 = Options()
# disable_all_extensions1.add_argument('--disable-extensions')
# driver_4 = webdriver.Firefox(executable_path='c:\\geckodriver.exe', options=disable_all_extensions1)
