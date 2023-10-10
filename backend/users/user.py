from backend.shopping_cart import shoppingCart
from backend.login import login


class user:

    def __init__(self, userID, username, login):
        self.userID = int(userID)
        self.username = str(username)
        self.login = bool(login)

    def get_user_info(self):
        return f"UserID: {self.userID}, Username: {self.username}."

    def has_shopping_cart(self, shoppingCart):
        return shoppingCart is not None

    def user_login(self, login):
        if login == True:#alt; password == entered_password
            print("Sucessfully logged in.")
        else:
            print("couldn't log in.")