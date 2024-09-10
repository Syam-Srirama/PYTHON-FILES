import math
a=int(input("Enter a value:\n"))
b=int(input("Enter b value:\n"))
Add=a+b
print('The Sum of {} and {} is :{}\n'.format(a,b,Add))
Sub=a-b
print('The Difference of {} and {} is :{}\n'.format(a,b,Sub))
Pro=a*b
print('The Product of {} and {} is :{}\n'.format(a,b,Pro))
Div=a/b
print('The Quotient of {} and {} is :{}\n'.format(a,b,Div))
FloorDiv=a//b
print('The Floored Quotient of {} and {} is :{}\n'.format(a,b,FloorDiv))
Rem=a%b
print('The Remainder of {} and {} is :{}\n'.format(a,b,Rem))
Pow=math.pow(a,b)
print('{} to the power of {} is :{}\n'.format(a,b,Pow))
