n=int(input("Enter The Element \n"))
l=[]
sum=0
for i in range(0,n):
    e = int(input("Enter The Values :"))
    l.append(e)
    sum+=e
print(l)
print("The Sum of given element is :",sum)