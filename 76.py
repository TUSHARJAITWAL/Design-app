l=['hello',10,20,40,20,60,40,30]
d=[]
for i in l:
    if l.count(i)>1 and i not in d:
        d.append(i)
print(d)