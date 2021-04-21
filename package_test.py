from ECommerce.Buyer_Class import Buyer
from ECommerce.Seller_Class import Seller

out_option = True
seller = Seller()
buyer = Buyer()
while out_option:
    choice = input("Are you buyer or seller? b/s: ")
    if choice == "s":
        option = True
        while option:
            print("1. Update items")
            print("2. Show items")
            print("3.. Exit")
            choice = input("Enter option: ")
            if choice == "1":
                seller.update()
            elif choice == "2":
                seller.show()
            elif choice == "3":
                option = False
            else:
                print("Enter valid choice or get out..")
    elif choice =="b":
        option = True
        while option:
            print("1. Search items")
            print("2. Buy items")
            print("3.. Exit")
            choice = input("Enter option: ")
            if choice == "1":
                item_name = input("Enter name of product: ")
                buyer.search(seller,item_name)
            elif choice == "2":
                buyer.buy(seller)
            elif choice == "3":
                option = False
            else:
                print("Enter valid choice or get out..")
    else:
        out_option = False
        print("Exiting system....Thank you for staying....")