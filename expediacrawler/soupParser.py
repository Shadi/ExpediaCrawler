from bs4 import BeautifulSoup

PROCESSOR = 'lxml'

OFFERS_CLASS = 'offer-listing'
PRICE_CLASS = 'dollars'
FLIGHT_DURATION_CLASS = 'duration-emphasis'
LAYOVR_CLASS = ''
AIRLINE_CLASS = ''


def parse_offers_page(html_content):
    offers_list = parse_offers_list(html_content)
    prices_list = []
    for offer in offers_list:
        offer_object = get_offer_object(offer)
        if offer_object is not None:
            prices_list.append(offer_object)
    return prices_list


def parse_offers_list(html_content):
    soup = BeautifulSoup(html_content, PROCESSOR)
    offers = soup.find_all('li', class_=OFFERS_CLASS)
    return offers


def get_offer_object(offer_html):
    offer_price = get_offer_price(offer_html)
    offer_duration = get_offer_duration(offer_html)
    offer_airline = get_offer_airline(offer_html)
    if offer_price is not None and offer_duration is not None and offer_airline is not None:
        return {'price': offer_price.strip(), 'duration': offer_duration.strip(), 'airline': offer_airline.strip()}


def get_offer_price(offer_html):
    offer_element = find_element_using_class(offer_html, 'span', PRICE_CLASS)
    if offer_element is not None:
        return find_element_using_class(offer_html, 'span', PRICE_CLASS).text


def get_offer_duration(offer_html):
    return find_element_using_class(offer_html, 'div', FLIGHT_DURATION_CLASS).text


def find_elements_using_class(html_content, element, css_class):
    soup = BeautifulSoup(html_content, PROCESSOR)
    return soup.find_all(element, class_=css_class)


def find_element_using_class(html_content, element, css_class):
    return html_content.find(element, class_=css_class)


def get_offer_airline(offer_html):
    return offer_html.find('div', {'data-test-id': 'airline-name'}).text
