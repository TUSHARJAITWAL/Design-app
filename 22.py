n=50
c1=0
c2=0
even=[]
odd=[]
for i in range(1,n+1):
    if(i%2==0):
        c1+=1
        even.append(i)
    else:
        c2+=1
        odd.append(i)
print("All Even Number is :-",c1)
print(even)
print("All Odd Number is:-",c2)
print(odd)
