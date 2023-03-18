n = int(input("Enter The Number :\n"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if(sum==n):
    print("Number is perfect")
else:
    print("Number is not perfect")