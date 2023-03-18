n = input("Enter The String \n")
vowels=0
v=[]
consonant=0
c=[]
result=""
for i in n:
    if i!=" ":
        result+=i
a1=['a','e','i','o','u','A','E','I','O','U']
for i in result:
    if i in a1:
        vowels+=1
        
    else:
        consonant+=1
print("The Vowles of given string is ",vowels)
print("The Consonant of given string is ",consonant)
