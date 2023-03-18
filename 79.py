s="aaabbcccc"
s1=""
ch=s[0]
count=0
for i in s:
    if i==ch:
        count+=1
    else:
        s1=s1+str(count)+ch
        count=1
        ch=i
s1=s1+str(count)+ch 
print(s1)   