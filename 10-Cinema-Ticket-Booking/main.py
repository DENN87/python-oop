import random
import sqlite3
import string


class User:
    """Represents a user that can buy a cinema Seat"""
    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):
        """Buys the ticket if the card is valid"""
        if seat.is_free():
            if card.validate(price=seat.get_price()):
                seat.occupy()
                ticket = Ticket(user=self, price=seat.get_price(), seat_number=seat_id)
                ticket.to_pdf()
                return "Purchase successful!"
            else:
                return "There was a problem with your card!"
        else:
            return "Seat is taken!"


class Seat:
    """Represents a cinema seat that can be taken from a User"""
    database = "cinema.db"

    def __init__(self, seat_id):
        self.seat_id = seat_id

    def get_price(self):
        """Get the price of a certain seat"""
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""SELECT "price" FROM "Seat" WHERE "seat_id"=?""", [self.seat_id])
        price = cursor.fetchall()[0][0]
        return price

    def is_free(self):
        """Check in the database if a Seat is taken or not"""
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""SELECT "taken" FROM "Seat" WHERE "seat_id"=?""", [self.seat_id])
        result = cursor.fetchall()[0][0]

        if result == 0:
            return True
        else:
            return False

    def occupy(self):
        """Change value of taken in the database from 0 to 1 if Seat is free"""
        if self.is_free():
            connection = sqlite3.connect(self.database)
            connection.execute("""UPDATE "Seat" SET "taken"=? WHERE "seat_id"=? """, [1, self.seat_id])
            connection.commit()
            connection.close()

class Card:

    database = "banking.db"

    def __init__(self, type, number, cvc, holder):
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder

    def validate(self, price):
        """Checks if Card is valid and has balance. Subtracts price from balance"""
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""SELECT "balance" FROM "Card" WHERE "number"=? and "cvc"=? """, [self.number, self.cvc])
        result = cursor.fetchall()

        if result:
            balance = result[0][0]
            if balance >= price:
                connection.execute("""UPDATE "Card" SET "balance"=? WHERE "number"=? and "cvc"=? """,
                                   [balance - price, self.number, self.cvc])
                connection.commit()
                connection.close()
                return True


class Ticket:

    def __init__(self, user, price, seat_number):
        self.id = "".join([random.choice(string.ascii_letters) for i in range(8)])
        self.user = user
        self.price = price
        self.seat_number = seat_number

    def to_pdf(self):
        pass


if __name__ == "__main__":

    name = input("Your full name: ")
    seat_id = input("Preferred seat number: ")
    card_type = input("Your card type: ")
    card_number = input("Your card number: ")
    card_cvc = input("Your card CVC: ")
    card_holder = input("Card holder name: ")

    print(name, seat_id)
    print(card_type, card_number, card_cvc, card_holder)

    user = User(name=name)
    seat = Seat(seat_id=seat_id)