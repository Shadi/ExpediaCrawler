def build_url(origin_city, destination_city, start_date, return_date):
    return "https://www.expedia.com/Flights-Search?trip=roundtrip&leg1=from:{org_city},to:{dest_city}," \
           "departure:{origin_date}TANYT&" \
           "leg2=from:{dest_city},to:{org_city},departure:{return_date}TTANYT&passengers=adults:1&mode=search" \
        .format(org_city=origin_city, dest_city=destination_city, origin_date=start_date, return_date=return_date)
