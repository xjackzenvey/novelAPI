from selenium import webdriver
from selenium.webdriver.edge.service import Service as edgeSrv
from selenium.webdriver.chrome.service import Service as chromeSrv
import time

'''
 #the function to setup an selenium browser.
 #browser supports 'edge' or 'chrome' only.
'''
def setupSelenium(browser:str,driver_path:str ):
    if browser == 'edge':
        _options = webdriver.EdgeOptions()
        _options.add_argument("--headless")
        _options.add_argument("--disable-blink-features")
        _options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Edge(
            options = _options,
            service = edgeSrv(executable_path=driver_path)
        )
        return driver
    
    elif browser == 'chrome':
        _options = webdriver.ChromeOptions()
        _options.add_argument("--disable-blink-features")
        _options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(
            options = _options,
            service = chromeSrv(executable_path=driver_path)
        )
        return driver
    
#the function to get a url:
def getHtml(url:str,driver,sleep_time:float):
    driver.get(url)
    time.sleep(sleep_time)                         #wait for javascript rendering
    return driver.page_source
