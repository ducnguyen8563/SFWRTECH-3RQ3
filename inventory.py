class inventory
    def __init__(self,name):
        self.name = name
        self.stock = True
        self.price = 5

    def no_stock(self):
        self.stock = False