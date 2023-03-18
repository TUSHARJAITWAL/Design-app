a = ['ajay','jay','ram']
b = ['sanu','ajay','ram']
arr = a+b
print(arr)
arr1 = []
for i in arr:
    if i not in arr1:
        arr1.append(i)
print(arr1)