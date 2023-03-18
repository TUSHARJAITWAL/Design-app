a=[1,2,5,9,13,17,12,13,3,8,29]
a1=[]
sum=0
for i in a:
    fact=0
    for j in range(1,i+1):
        if i%j==0:
            fact+=1
    if(fact==2):
        a1.append(i)
        sum+=i
print("All Prime Number is :",a1)
print("Sum of a prime number is :",sum)