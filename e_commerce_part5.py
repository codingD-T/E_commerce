# for
# while

 # initialization increment terminating
# for i in [1,23.5]:
#     print(i)

# option = True
# while option:
#     print(option)

option = True
data = {}
while option:
    print("1. Update items")
    print("2. Show items")
    print("3. Exit")
    choice = input("Enter option: ")
    if choice =="1":
        item_name = input("Enter name: ")
        item_quantity = input("Enter quantity: ")
        data[item_name] = item_quantity
    elif choice == "2":
        print("Showing items....")
        for i,j in data.items():
            print(i,j)
    elif choice == "3":
        option = False
    else:
        print("Enter valid choice or get out..")