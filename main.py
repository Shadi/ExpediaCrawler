import seleniumReader
import soupParser

full_content = seleniumReader.getHtml(
    "https://www.expedia.com/Flights-Search?trip=roundtrip&leg1=from:HAM,to:AMM,departure:03/08/2017TANYT&leg2=from:AMM,to:HAM,departure:03/24/2017TANYT&passengers=adults:1&mode=search")
offers = soupParser.parse_offers_page(full_content)

for offer in offers:
    print(offer)
