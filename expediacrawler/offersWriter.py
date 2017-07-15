import csv


def write_offers(all_offers, results_file):
    if results_file:
        append_to_csv(all_offers, results_file)
    for day in all_offers:
        print(day, ":")
        for offer in all_offers[day]:
            print(offer)


def append_to_csv(all_offers, file_name):
    with open(file_name, 'a') as f:
        writer = csv.writer(f)
        for day in all_offers:
            for offer in all_offers[day]:
                offer_info = list(offer.values());
                offer_info.append(day)
                writer.writerow(offer_info)
