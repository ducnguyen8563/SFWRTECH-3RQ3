from ProjectDeliverable.item import Item


# Requirement: discount of 5% is applied on shop's side
def test_discount_five_percent():
    discount = 0.05

    assert item.price == 0.05* item.price, "discount should be 5%!"

# Requirement: discount of 5% is applied on shop's side
def test_discount_five_percent():
    discount = 0.10

    assert item.price == 0.05* item.price, "discount should be 10%!"

#test price filter
def test_filter()
    lowerFilter = 100
    higherFilter = 500
    itemprice = Item.price

    while lowerFilter<itemprice<higherFilter ()
        display.Items()

        assert message == "there should be no items with price lower than lowerFilter or higher than higherFilter"