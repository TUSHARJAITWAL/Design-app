n=100
count=0
prime=[]
for i in range(1,n+1):
    fact=0
    for j in range(1,i+1):
        if i%j==0:
            fact+=1
    if(fact==2):
        count+=1
        prime.append(i)
print("1 to 100 all prime number is :",count)
print(prime)