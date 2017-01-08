import time  
from bs4 import BeautifulSoup
from selenium import webdriver


browser = webdriver.Firefox()

ffResults = browser.get("https://www.expedia.com/Flights-Search?trip=roundtrip&leg1=from:Hamburg,%20Germany%20(HAM-All%20Airports),to:Amman,%20Jordan%20(AMM-Queen%20Alia%20Intl.),departure:03/08/2017TANYT&leg2=from:Amman,%20Jordan%20(AMM-Queen%20Alia%20Intl.),to:Hamburg,%20Germany%20(HAM-All%20Airports),departure:03/24/2017TANYT&passengers=adults:2,children:0,seniors:0,infantinlap:Y&mode=search")

time.sleep(15)

full_content = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")

browser.quit()

soup = BeautifulSoup(full_content, "lxml" )

print(soup.find_all('span', class_='dollars'))

#for dollar in dollars_copy:
#    print(dollar.text)
#print(dollars)

#print(result)
