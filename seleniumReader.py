import time
from selenium import webdriver
from pyvirtualdisplay import Display


def getHtml(url):
    display = Display(visible=0, size=(800, 600))
    display.start()
    browser = webdriver.Firefox()
    ffResults = browser.get(url)
    time.sleep(30)
    full_content = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    browser.quit()
    display.stop()
    return full_content
