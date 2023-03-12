import unittest
from datetime import date, datetime
from reservations import Reservations
from hotel import Hotel
from guest import Guest


class TestReservations(unittest.TestCase):

    def test_reservation_not_through(self):
        start_date = date(2023, 3, 23)
        end_date = date(2023, 3, 26)
        room_type = "Cheap room"
        hotel = Hotel("hotel_reservations_test")
        retval = hotel.check_availability(start_date, end_date, room_type)
        self.assertEqual(retval, False)

    def test_reservation_through(self):
        start_date = date(2023, 3, 15)
        end_date = date(2023, 3, 20)
        room_type = "Cheap room"
        hotel = Hotel("hotel_reservations_test")
        retval = hotel.check_availability(start_date, end_date, room_type)
        self.assertEqual(retval, True)

    def test_reservation_through_same_day_in(self):
        start_date = date(2023, 3, 15)
        end_date = date(2023, 3, 23)
        room_type = "Cheap room"
        hotel = Hotel("hotel_reservations_test")
        retval = hotel.check_availability(start_date, end_date, room_type)
        self.assertEqual(retval, True)

    def test_reservation_through_same_day_out(self):
        start_date = date(2023, 3, 26)
        end_date = date(2023, 3, 30)
        room_type = "Cheap room"
        hotel = Hotel("hotel_reservations_test")
        retval = hotel.check_availability(start_date, end_date, room_type)
        self.assertEqual(retval, True)

    def test_reservation_length(self):
        start_date = date(2023, 3, 30)
        end_date = date(2023, 3, 31)
        guest = "Alex"
        room_type = "Expensive room"
        comments = "Champagne bottle in room"
        reservation = Reservations(guest, start_date, end_date, room_type, comments)
        self.assertEqual(reservation.get_reservation_length(), 1)

    def test_price(self):
        start_date = date(2023, 3, 31)
        end_date = date(2023, 4, 3)
        guest = "Alex"
        room_type = "Expensive room"
        comments = "Champagne bottle in room"
        reservation = Reservations(guest, start_date, end_date, room_type, comments)
        self.assertEqual(reservation.get_price(), 90)

    def test_read_from_file_hotel(self):
        hotel = Hotel("hotel_reservations_test")
        retval = hotel.read_previous_reservations("hotel_reservations_test")
        start_date = date(2023, 3, 23)
        end_date = date(2023, 3, 26)
        list = [["0442046661","Alex Mecklin","alex.mecklin@hotmail.com","Cheap room",start_date,end_date,"comments"]]
        self.assertEqual(retval, list)

    def test_read_from_file_guest(self):
        guest = Guest("Alex Mecklin", "0442046661", "alex.mecklin@hotmail.com", "guest_reservations_test")
        retval = guest.read_previous_guest_reservations("guest_reservations_test")
        self.assertEqual(retval, [['2023-3-23', '2023-3-26', 'Cheap room'], ['2023-3-15', '2023-3-20', 'Cheap room']])

    def test_printing_interval(self):
        hotel = Hotel("hotel_reservations_test")
        start_date = date(2023, 3, 20)
        end_date = date(2023, 3, 25)
        retval = hotel.print_reservations_in_interval(start_date, end_date)
        self.assertEqual(retval, "0442046661, Alex Mecklin, alex.mecklin@hotmail.com, Cheap room, 2023-03-23, 2023-03-26, comments\n")

    def test_make_reservation(self):
        start_date = date(2023, 3, 10)
        end_date = date(2023, 3, 15)
        room_type = "Cheap room"
        comments = "Test"
        name = "Alex"
        email = "test@hotmail.com"
        phone_nr = "112"
        hotel = Hotel("hotel_reservations_test")
        retval = hotel.make_reservation(start_date, end_date, room_type, comments, name, phone_nr, email)
        self.assertEqual(retval, True)

