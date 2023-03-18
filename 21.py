n=100
even=[]
odd=[]
for i in range(1,n+1):
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("All Even Number is:-",even)
print("All Odd Number is:-",odd)