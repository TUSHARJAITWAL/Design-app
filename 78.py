str1='a,a,a,b,b,c,c,c,c'
str2=str1.split(",")
str3=[]
for i in str2:
    if i not in str3:
        print(i,':',str2.count(i),end="")
        str3.append(i)


