num1=int(input("Enter The first number :\n"))
num2=int(input("Enter The second number :\n"))
num3=int(input("Enter The third number :\n"))
if(num1>num2):
    if(num1>num3):
        print("Num1 is greater")
    else:
        print("Num3 is greater")
else:
    if(num2>num3):
        print("num2 is greater")
    else:
        print("num3 is greater")