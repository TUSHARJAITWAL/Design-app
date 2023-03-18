a = [4,3,2,5,0,9,3,2]
for i in range(0,len(a)):
    for j in range(i,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)
        
        