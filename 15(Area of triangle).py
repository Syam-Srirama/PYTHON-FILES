import math
a=int(input("Enter the first side"))
b=int(input("Enter the first side"))
c=int(input("Enter the first side"))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print('The area of the given triangle is:{}'.format(area))
