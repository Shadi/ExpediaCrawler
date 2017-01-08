import time  
from selenium import webdriver

def getHtml(url):
    browser = webdriver.Firefox()
    ffResults = browser.get(url)
    time.sleep(5)
    full_content = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")  
    browser.quit()
    return full_content
