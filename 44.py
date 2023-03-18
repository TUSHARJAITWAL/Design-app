n = input("Enter The Number :\n")
vowels=[]
consonant=[]
result=""
for i in n:
    if i!=" ":
        result+=i
a1=['a','e','i','o','u','A','E','I','O','U']
for i in result:
    if i in a1:
        vowels.append(i)
    else:
        consonant.append(i)
print("Given String Vowels is")
print(vowels)
print("Given String Consonant is")
print(consonant)
    