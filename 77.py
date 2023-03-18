str1="a3b2c4"
str2=""
for i in str1:
    if i.isalpha():
        var=i
    else:
        n=int(i)
        str2=str2+(var*n)
print(str2)


    