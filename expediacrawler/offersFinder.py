import expediacrawler.soupParser as soupParser
import expediacrawler.urlBuilder as urlBuilder
from expediacrawler.dateCalculator import calculate_new_dates
from expediacrawler.offersWriter import print_offers_stdout


def find_offers(orig_city, dest_city, leave, back, forward_days):
    all_offers = get_offers(orig_city, dest_city, leave, back, forward_days)
    print_offers_stdout(all_offers)


def get_offers(orig_city, dest_city, leave, back, forward_days):
    all_offers = {}
    day_offer = get_day_offers(orig_city, dest_city=dest_city, leave=leave, back=back)
    all_offers[leave + "-" + back] = day_offer[0:5]
    for i in range(1, forward_days + 1):
        print("Reading element: {order} ....".format(order=i))
        out_str, return_str = calculate_new_dates(leave, back, i)
        day_offer = get_day_offers(orig_city, dest_city=dest_city, leave=out_str, back=return_str)
        all_offers[out_str + '-' + return_str] = day_offer[0:5]
    return all_offers


def get_day_offers(orig_city, dest_city, leave, back):
    url = urlBuilder.build_url(origin_city=orig_city, destination_city=dest_city,
                               start_date=leave, return_date=back)
    return soupParser.get_page_offers(url)
