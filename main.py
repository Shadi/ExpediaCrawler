import urllib.request

result=urllib.request.urlopen("https://www.expedia.de/Flights-Search?trip=roundtrip&leg1=from:Hamburg,%20Deutschland%20(HAM-Alle%20Flugh%C3%A4fen),to:Amman,%20Jordanien%20(AMM-Queen%20Alia%20Intl.),departure:08.03.2017TANYT&leg2=from:Amman,%20Jordanien%20(AMM-Queen%20Alia%20Intl.),to:Hamburg,%20Deutschland%20(HAM-Alle%20Flugh%C3%A4fen),departure:26.03.2017TANYT&passengers=children:0,adults:2,seniors:0,infantinlap:Y&mode=search").read()

print(result)
