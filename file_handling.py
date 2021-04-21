# f = open('file.txt',"r")
# print(f.readlines())
# f.close()

with open('file.txt',"r") as f:
    print(f.read())
    print(f.readlines())
