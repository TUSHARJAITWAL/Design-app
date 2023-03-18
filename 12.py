n = 1234
i=1
rev=0
while i<=n:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)

n=1234
rev=0
for i in range(1,-1,n+1):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev) 