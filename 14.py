n = int(input("Enter The Number :\n"))
i=1
fact=0
while i<=n:
    if n%i==0:
        fact+=1
    i+=1
if(fact==2):
    print("Number is prime")
else:
    print("Number is not prime")