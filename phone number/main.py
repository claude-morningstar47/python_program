import phonenumbers
from test import list_nmber

from phonenumbers import geocoder, carrier

for number in list_nmber:
    ch_nmber = phonenumbers.parse(number, "CH")
    print(geocoder.description_for_number(ch_nmber, "en"))

    service_nmber = phonenumbers.parse(number, "RO")
    print(carrier.name_for_number(service_nmber, "en"))
    print("--------------------------")
