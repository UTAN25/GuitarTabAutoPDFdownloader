import requests
import re
import shutil
from selenium import webdriver
import time
import pyautogui

def Koplortu():
    html = driver.page_source
    a=re.search(r'<div class="_3Apiz pGGuZ">\d\d(\d)?</div>',html)

    return re.search(r'\d\d(\d)?',a.group()).group()




url='https://www.ultimate-guitar.com/user/mytabs'

driver = webdriver.Firefox()
driver.get(url)

elem = driver.find_element_by_css_selector('._3Oqhz')
elem.click()
elem = driver.find_element_by_css_selector('._3K_s7')
elem.click()

textua = driver.find_element_by_css_selector('.lNOf1 > div:nth-child(1) > input:nth-child(1)')
textua.send_keys(input('Erabiltzailea:'))

textua = driver.find_element_by_css_selector('._2ZaFT > div:nth-child(1) > input:nth-child(1)')
pasahitza=input('Pasahitza:')
for i in range(40):
    print('\n')
textua.send_keys(pasahitza)

elem = driver.find_element_by_css_selector('.lNOf1 > div:nth-child(3) > button:nth-child(1)')
elem.click()

elem = driver.find_element_by_css_selector('a._1KmPn:nth-child(1)')
elem.click()

kop=int(Koplortu())
for i in range(24,kop):
    n=str(2+i)
    elem = driver.find_element_by_css_selector('div.pZcWD:nth-child('+n+') > div:nth-child(2) > header:nth-child(1) > span:nth-child(1) > span:nth-child(1) > a:nth-child(1)')
    elem.click()
    elem = driver.find_element_by_css_selector('.TVSW7 > button:nth-child(1)')
    elem.click()
    elem = driver.find_element_by_css_selector('.enzw_ > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)')
    elem.click()
    time.sleep(6)

    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('Captura2.PNG')))


    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('Captura.PNG')))

    driver.back()
