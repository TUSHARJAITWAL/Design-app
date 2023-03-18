n = int(input("Enter The Number :\n"))
fact=1
i=1
count = 0
while i<=n:
    fact*=i
    i+=1
x = str(fact)
print("The value of factorial {} is :".format(n),x)
y=x
for i in y:
    if i!='0':
        count+=1
print("The Non zero Number is : ",count)