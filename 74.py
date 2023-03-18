s = "sky is blue"
s1=s.split()
print(s1)
s1=s1[::-1]
print(s1)
s2=" ".join(s1)
print(s2)

s="sky is blue"
s1=s.split()
s2=[]
for i in range(len(s1)-1,-1,-1):
    s2.append(s1[i])
s3=" ".join(s2)
print(s3)



