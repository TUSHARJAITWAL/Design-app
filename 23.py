a = [1,2,3,4,5,6,7,8,9,10,25,13,37,12,19,63,66,59,88]
even=[]
odd=[]
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even is :--",even)
print("Odd is :--",odd)