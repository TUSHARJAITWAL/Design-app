a = float(input("Enter The first side : "))
b= float(input("Enter The Second side : "))
c = float(input("Enter The Third side : "))

# calculate the semi-perimeter
s = (a+b+c)/2

# calculate the area of Triangle
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("The Area of Triangle is :",area)
