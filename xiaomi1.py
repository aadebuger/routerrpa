from selenium import webdriver # 从selenium导入webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time

def login():

    passpath="""//*[@id="password"]"""
    elem = driver.find_element_by_xpath(passpath)
    elem.clear()
    print("elem=",elem)
    elem.send_keys("****")
    loginpath="""//*[@id="btnRtSubmit"]"""
    elem = driver.find_element_by_xpath(loginpath)
    elem.click()
    time.sleep(10)
    pageSource = driver.page_source
#    print("pageSource",pageSource)
    fileToWrite = open("page_source1.html", "w")
    fileToWrite.write(pageSource)
    fileToWrite.close()
def sysmenu():
    menupath="""//*[@id="sysmenu"]"""
    elem = driver.find_element_by_xpath(menupath)
    print("menu elem ",elem )
    elem.click()

def reboot():
    rebootpath="""//*[@id="toReboot"]"""
    elem = driver.find_element_by_xpath(rebootpath)
    print("elem ",elem )
    elem.click()
    time.sleep(5)
    pageSource = driver.page_source
#    print("pageSource",pageSource)
    fileToWrite = open("page_source2.html", "w")
    fileToWrite.write(pageSource)
    fileToWrite.close()

def rebootaction():
#rebootAction
    rebootpath="""//*[@id="rebootAction"]"""
    elem = driver.find_element_by_xpath(rebootpath)
    print("rebootAction elem ",elem )
    elem.click()
    time.sleep(5)
    pageSource = driver.page_source
    print("pageSource3",pageSource)
    fileToWrite = open("page_source3.html", "w")
    fileToWrite.write(pageSource)
    fileToWrite.close()

def rebootconfirmold():
    a= driver.switch_to.alert
    print("alert text",a.text)
    prompt=a.text
    driver.switch_to.alert.accept()

def rebootjs():

	js_reboot="reboot_window(false);"
	ret=driver.execute_script(js_reboot)
	print("rebootjs ret",ret)

options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/google-chrome'
options.add_argument('headless')
options.add_argument('window-size=1200x600')
#options.add_argument("--lang=en-GB");
#options.add_argument("start-maximized"); 
#options.add_argument("disable-infobars"); 
options.add_argument("--disable-extensions"); 
options.add_argument("--disable-gpu"); 
#options.add_argument("--disable-dev-shm-usage"); 
options.add_argument("--no-sandbox");
driver = webdriver.Chrome(chrome_options=options)  # Optional argument, if not specified will search path.

driver.get('http://192.168.31.1')
pageSource = driver.page_source
#print("pageSource",pageSource)
fileToWrite = open("page_source.html", "w")
fileToWrite.write(pageSource)
fileToWrite.close()
time.sleep(5)
login()
time.sleep(5)
sysmenu()
time.sleep(15)
reboot()
time.sleep(5)
rebootaction()

time.sleep(5)
rebootjs()
