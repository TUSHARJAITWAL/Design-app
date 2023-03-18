# a2=input("Enter The Number :\n")
a="nayan"
a1=""
for i in range(len(a)-1,-1,-1):
    a1+=a[i]
if(a1==a):
    print("Given String is palindrome")
else:
    print("Given String is not plindorme")