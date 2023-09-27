from ..shopping_cart import shoppingCart
from ..login import login


class user:

    def __init__(self, userID, username):
        self.userID = userID
        self.username = username

        def __str__(self):
            return f"UserID: {self.userID}, Username: {self.username}."

        def get_id(self):
            return str(self.userID)

        def has_shopping_cart(self, shoppingCart):
            pass

        def user_login(self, login):
            pass



