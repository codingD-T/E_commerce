option = True
data = {}
def update(data):
    item_name = input("Enter name: ")
    item_quantity = input("Enter quantity: ")
    data[item_name] = item_quantity
def show(data):
    print("Showing items....")
    for i, j in data.items():
        print(i, j)
def search(data,key):
    return data.get(key)
while option:
    print("1. Update items")
    print("2. Show items")
    print("3. Search item")
    print("4. Exit")
    choice = input("Enter option: ")
    if choice == "1":
        update(data)
    elif choice == "2":
        show(data)
    elif choice == "3":
        key=input("Enter the item to be searched: ")
        print(search(data, key))
    elif choice == "4":
        option = False
    else:
        print("Enter valid choice or get out..")