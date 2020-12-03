class Cart:
    def __innit__(self):
        self.cart = []

    def __len__(self):
        return len(self.cart)

    def add_item(self,item):
        if item.stock:
            self.cart.append(item)
        else:
            return "Sorry, there is no stock left."

    def add_multiple(self, items):
        for item in items:
            self.cart.append(item)