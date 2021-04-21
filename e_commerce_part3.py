#li = [1,2,"Hello",True]
# print(li)
# print(type(li))
# print(li[2])
# li2 = ["Hey",67,98.9]
# li.extend(li2)
# li.append("Good Day")

x = input("Enter price of 1st item: ")
y = input("Enter price of 2nd item: ")
add = int(x) + int(y)
tax = add*0.1
total = add + tax
if total >= 1000:
    total = total - total*0.1
elif total>=500 and total<1000:
    total = total - total*0.07
else:
    pass

print(total)
li =["Milk","Notebooks","Maggi"]


user = ["User1"]