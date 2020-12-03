#Cart functionalities.
from ProjectDeliverable.item import Item
from ProjectDeliverable.cart import Cart

#test adding item to cart
def test_add_item_to_cart():
    cart = Cart()
    assert len(cart) == 0, "cart should not have any item at the start"

    item = Item("Z390 Asus")
    cart.add_item(item)

    assert len(cart) == 1, "The cart should only add 1 item"

#test adding not available item to cart
def test_add_unavailable_item_to_cart():
    cart = Cart()
    assert len(cart) == 0, "cart should not have any item at the start"

    item = Item("Z390 Asus")
    item.stock()
    cart.add_item(item)

    assert len(cart) == 0, "the cart will not add item if it is not in stock"

#test unavailable item error message
def test_adding_unavailable_item_error_message():
    cart = Cart;
    assert len(cart) == 0, "cart should not have any item at the start"

    item= Item("Z390 Asus")
    item.nostock()
    message = cart.add_item(item)

    assert message == "This item is not in stock", "Should receive an error message"

#test adding multiple items at once to cart
def test_add_multiple_quantity_to_cart()
    cart = Cart();
    assert len(cart) == 0, "cart should not have any item at the start"

    item = [Item("Z390 Asus"), Item("Z390 Asus"), Item("MSI RTX3080")]
    cart.add_item(item)

    assert len(cart) == 3, "Cart should now have 2 Z390 Asus Motherboards and one MSI RTX3080"

    item = [Item("Z390 Asus"), Item("Z390 Asus"), Item("MSI RTX3080")]
    cart.add_item(item)


#test removing items from cart
def remove_item_from_cart()
    cart = Cart();
    CartCount = len(cart)

    if(CartCount>=1)
        CartCount = len(cart)-1
    else
        CartCount == 0

#check to see if total price adds up.
def totalPrice(totalPrice)
    CartCount = len(cart)

    itemCount = 0
    while (itemCount != CartCount)
    Item.price(totalPrice)+=1
    itemCount+=1

    return totalPrice;
assert message = "The total price should be the price of all items in cart"