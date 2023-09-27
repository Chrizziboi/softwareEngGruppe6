from backend.shopping_cart import shoppingCart
from backend.login import login


class user:

    def __init__(self, userID, username):
        self.userID = int(userID)
        self.username = str(username)

    def get_user_info(self):
        return f"UserID: {self.userID}, Username: {self.username}."

    def get_id(self):
        return str(self.userID)

    def has_shopping_cart(self, shoppingCart):
        return shoppingCart is not None

    def user_login(self, login):
        return True





