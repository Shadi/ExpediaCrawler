from bs4 import BeautifulSoup

__PROCESSOR = 'lxml'

__OFFERS_CLASS = 'offer-listing'
__PRICE_CLASS = 'dollars'
__FLIGHT_DURATION_CLASS = 'duration-emphasis'
__LAYOVR_CLASS = ''
__AIRLINE_CLASS = ''


def parse_offers_page(html_content):
    offers_list = __parse_offers_list(html_content)
    prices_list = []
    for offer in offers_list:
        offer_object = __get_offer_object(offer)
        if offer_object is not None:
            prices_list.append(offer_object)
    return prices_list


def __parse_offers_list(html_content):
    soup = BeautifulSoup(html_content, __PROCESSOR)
    offers = soup.find_all('li', class_=__OFFERS_CLASS)
    return offers


def __get_offer_object(offer_html):
    offer_price = __get_offer_price(offer_html)
    offer_duration = __get_offer_duration(offer_html)
    offer_airline = __get_offer_airline(offer_html)
    if offer_price is not None and offer_duration is not None and offer_airline is not None:
        return {'price': offer_price.strip(), 'duration': offer_duration.strip(), 'airline': offer_airline.strip()}


def __get_offer_price(offer_html):
    offer_element = __find_element_using_class(offer_html, 'span', __PRICE_CLASS)
    if offer_element is not None:
        return __find_element_using_class(offer_html, 'span', __PRICE_CLASS).text


def __get_offer_duration(offer_html):
    return __find_element_using_class(offer_html, 'div', __FLIGHT_DURATION_CLASS).text


def __find_elements_using_class(html_content, element, css_class):
    soup = BeautifulSoup(html_content, __PROCESSOR)
    return soup.find_all(element, class_=css_class)


def __find_element_using_class(html_content, element, css_class):
    return html_content.find(element, class_=css_class)


def __get_offer_airline(offer_html):
    return offer_html.find('div', {'data-test-id': 'airline-name'}).text
