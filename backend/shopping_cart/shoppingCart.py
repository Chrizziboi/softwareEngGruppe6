class shoppingCart:
    def __init__(self):
        self.tour = []


    def add_tour(self, tour_name, quantity, price):
        tour = tour_name, quantity, price
        self.tour.append(tour)

    def remove_tour(self, tour_name):
        for tour in self.tour:
            if tour[0] == tour_name:
                self.tour.remove(tour)
                break

    def show_tour(self):
        for tour in self.tour:
            print(f"Navn: {tour[0]} Qty: {tour[1]} Price: {tour[2]}")

    def calculate_price(self):
        total = 0
        for tour in self.tour:
            total += tour[2]
        return total


