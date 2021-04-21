class Buyer:
    def __init__(self):
        self.cart = {}
        self.quantity = {}
        self.total_amount = 0

    def search(self,seller,item_name):
        if seller.products_quantity.get(item_name):
            print("Quantity: "+ str(seller.products_quantity.get(item_name)))
            print("Price per product: " + str(seller.products_price.get(item_name)))
            choice = input("Do you want to add this in cart? y/n: ")
            if choice == "y":
                quantity = int(input("Enter quantity: "))
                if quantity > seller.products_quantity.get(item_name):
                    print("That quantity does not exist")
                    self.search(seller,item_name)
                else:
                    self.cart[item_name] = seller.products_price.get(item_name)*quantity
                    self.quantity[item_name] = quantity
                    self.total_amount += seller.products_price.get(item_name)*quantity
            else:
                pass
        else:
            return "Your requested product does not exist"


    def show(self):
        print("Showing items....")
        for i, j in self.cart.items():
            print(i, j)

    def buy(self,seller):
        print("These are the items in your cart....")
        self.show()
        print("Total payable amount is: " + str(self.total_amount))
        for item,quantity in self.quantity.items():
            seller.buy(item,quantity)