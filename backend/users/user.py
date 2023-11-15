from backend.shopping_cart import shoppingCart

class user:

    def __init__(self, userID, username): #parameter password for a system that would use password
        self.userID = int(userID)
        self.username = str(username)
        #self.password = str(password)
        self.shoppingCart = shoppingCart.shoppingCart

    def get_user_info(self):
        return f"UserID: {self.userID}, Username: {self.username}."

    def get_username(self):
        return self.username
    def get_userID(self):
        return self.userID

    def has_shopping_cart(self):
        if len(self.shoppingCart.tour) > 0:
            shoppingCart.shoppingCart.show_tour()
        else:
            return f"Bruker {self.username} har ingen handlekurv"

'''
     def user_login(self, password):
        if password == entered_password
            print("Sucessfully logged in.")
        else:
            print("couldn't log in.")
'''