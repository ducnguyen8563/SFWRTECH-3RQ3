from ProjectDeliverable.inventory import Inventory
from ProjectDeliverable.cart import Cart
from ProjectDeliverable.item import Item

def test_remove_cart_with_one_item_from_inventory():
    cart = Cart()
    assert len(cart)

    item = Item("Z390 Asus")
    inventory.remove_item(item)

    assert len(cart) == 1, "The iventory of that item will be removed after it is processed in cart"

def test_remove_cart_with_multiple_item_from_inventory():
    cart = Cart();

    item = [Item("Z390 Asus"), Item("Z390 Asus"), Item("MSI RTX3080")]
    inventory.remove_item(item)

    assert len(cart) == 3, "Inventory should have removed multiple items presented in cart"

    item = [Item("Z390 Asus"), Item("Z390 Asus"), Item("MSI RTX3080")]
    inventory.remove_item(item)