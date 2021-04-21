class Seller:
    def __init__(self):
        self.products_quantity = {}
        self.products_price = {}
        self.profit = 0

    def update(self):
        item_name = input("Enter name: ")
        item_quantity = int(input("Enter quantity: "))
        item_price = int(input("Enter selling price: "))
        self.products_quantity[item_name] = item_quantity
        self.products_price[item_name] = item_price

    def show(self):
        print("Showing items....")
        for i, j in self.products_quantity.items():
            print(i, j)

    def buy(self,item_name,quantity):
        if quantity > self.products_quantity.get(item_name):
            print("Sorry We dont have that quantity")
        else:
            self.products_quantity[item_name] = self.products_quantity.get(item_name) - quantity
            self.profit += self.products_price.get(item_name)*quantity