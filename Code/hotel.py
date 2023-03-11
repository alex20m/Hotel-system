from guest import Guest
from datetime import date
from cheap_room import CheapRoom
from normal_room import NormalRoom
from expensive_room import ExpensiveRoom
from guest import Guest


class Hotel:

    """
    We use the guests phone numbers to identify the guests, since guests can have the same names, but
    they can't have the same phone number.

    hotel_reservations is a dictionary with all the hotels reservations. The key is the guests phone number
    and the values are a list where the first element is the guests name, the second is element is
    check in date, the third element is checkout date, fourth element is room type and
    fifth element is comments made by guest when booking.

    hotel_guests is a dictionary where the key is the guests phone number, the values are lists, where
    the first element is the guests name, the second is the guests email address.
    """

    def __init__(self):
        self.hotel_reservations = {}
        self.hotel_guests = {}
        self.cheap_room = CheapRoom()


    def read_previous_reservations(self):
        pass

    def check_availability(self, start_date, end_date):
        pass

    def print_reservations_in_interval(self, start_date, end_date):
        pass