def print_offers_stdout(all_offers):
    for day in all_offers:
        print(day, ":")
        for offer in all_offers[day]:
            print(offer)
