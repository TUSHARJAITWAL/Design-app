n = int(input("Enter The Number\n"))
fact=1
i=1
count=0
while i<=n:
    fact=fact*i
    i+=1
x = str(fact)
print("The Value of factorial",n,"is",x)
x.strip()
y=x
for j in y:
    if j != '0':
        count+=1
print("The non zero number is",count)
