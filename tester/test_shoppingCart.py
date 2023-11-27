from backend.shopping_cart import shoppingCart

"""testene fungerer, hvis de kjøres i shoppingcart filen
database koden må fjernes evt fra add_tour og remove_tour funksjonen"""
def test_item_not_in_shopping_cart():
    empty_cart = []
    shoppingcart = shoppingCart()
    assert (shoppingcart.__line__() == len(empty_cart))

def test_is_item_in_shopping_cart():
    empty_cart = []
    shoppingcart = shoppingCart()
    shoppingcart.add_tour("Botanisk Hage", 2, 200)
    assert (shoppingcart.__line__() is not empty_cart)