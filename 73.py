a = int(input("Enter The First Number :\n"))
b = int(input("Enter The Second Number :\n"))
c = int(input("Enter The Third Number :\n"))
if a<b:
    if a<c:
        print("a is smallest")
    else:
        print("c is smallest")
else:
    if b<c:
        print("b is smallest")
    else:
        print("c is smallest")
        