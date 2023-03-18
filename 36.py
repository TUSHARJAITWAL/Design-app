n=int(input("Enter The Number :\n"))
org=n
sum=0
while n!=0:
    rem=n%10
    fact=1
    for i in range(1,rem+1):
        fact=fact*i
    sum=sum+fact
    n=n//10
if(sum==org):
    print("Number is strong")
else:
    print("Number is not strong")
        