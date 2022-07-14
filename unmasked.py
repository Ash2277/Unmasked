import csv
import sys
from getpass import getpass
from time import sleep
import time
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from msedge.selenium_tools import Edge, EdgeOptions, options


def account_info():
    with open('account_info.txt', 'r') as f:
        info = f.read().split()
        email = info[0]
        password = info[1]
    return email, password


email, password = account_info()

options = EdgeOptions()
options.use_chromium = True
driver = Edge(options=options)

driver.get('https://twitter.com/explore')

time.sleep(1)

news = driver.find_element_by_xpath(
    '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[2]/nav/div/div[2]/div/div[4]/a/div/span').click()

# username = driver.find_element_by_xpath(
# '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
# username.send_keys(email)
# time.sleep(1)
# next1 = driver.find_element_by_xpath(
# '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div').click()
# username.send_keys(Keys.RETURN)
# my_password = getpass()

# password = driver.find_element_by_xpath('//input[@name="session[password]"]')
# password.send_keys('aashish@123')

# password.send_keys(Keys.RETURN)

# search_input = driver.find_element_by_xpath(
#     '//input[@aria-label-"Search query"]')
# search_input.send_keys('news')

# search_input.send_keys(Keys.RETURN)

card = driver.find_element_by_xpath(
    '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div[4]/div/div/div/div[1]/div[2]/span')
print(card)
