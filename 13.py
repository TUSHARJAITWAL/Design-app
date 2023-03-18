n = int(input("Enter The Number : \n"))
org=n
i=1
rev=0
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n = n//10
if(rev==org):
    print("Number is a palindorme")
else:
    print("Number is not palindorme")
    
