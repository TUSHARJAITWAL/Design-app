a = [1,3,4,5,2,6,8]
a1=[]
a2=[]
a3=[]
for i in a:
    if(i%2==0):
        a1.append(i)
    else:
        a2.append(i)
print("Even :--",a1)
print("Odd :--",a2)
for i in sorted(a1):
    a3.append(i)
for i in sorted(a2):
    a3.append(i)
print("Sorted Array is :--",a3)