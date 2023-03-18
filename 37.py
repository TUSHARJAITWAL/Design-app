n = int(input("Enter The Number :\n"))
i=1
sum=0
while i<n:
    if n%i==0:
        sum+=i
    i+=1
print(sum)
if(sum==n):
    print("Number is perfect")
else:
    print("Number is not perfect")