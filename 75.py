l = [1,2,2,3,3,4,5,5,5,6,6]
l1=[]
count=0
for i in l:
    if l.count(i)==1:
        l1.append(i)
print(l1)