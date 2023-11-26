from backend.database.db import get_db


class shoppingCart:
    def __init__(self, user):
        self.tour = []
        self.user = user


    def add_tour(self, tour_name, quantity, price):
        tour = tour_name, quantity, price
        self.tour.append(tour)
        conn = get_db()
        try:
            conn.execute(
                "INSERT INTO tours (userID, tour_name, quantity, price) VALUES (?, ?, ?, ?)",
                (self.user.get_userID(), tour_name, quantity, price)
            )
            conn.commit()
        finally:
            conn.close()

    def remove_tour(self, tour_name):
        for tour in self.tour:
            if tour[0] == tour_name:
                self.tour.remove(tour)
                break
        conn = get_db()
        try:
            conn.execute(
                "DELETE FROM tours WHERE userID = (?) AND tour_name = (?)",
                (self.user.get_userID(), tour_name)
            )
            conn.commit()
        finally:
            conn.close()

    def show_tour(self):
        for tour in self.tour:
            print(f"Navn: {tour[0]} Qty: {tour[1]} Price: {tour[2]}")

    def calculate_price(self):
        total = 0
        for tour in self.tour:
            total += tour[2]
        return total

