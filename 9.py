import math
a=int(input("Enter a value"))
b=int(input("Enter b value"))
add=a+b
sub=a-b
mul=a*b
div=a/b
floordiv=a//b
rem=a%b
power= math.pow(a,b)
print('Sum of %d and %d is %d'%(a,b,add))
print('Difference between %d and %d is %d'%(a,b,sub))
print('Product of %d and %d is %d'%(a,b,mul))
print('Actual Quotient when %d is divided by %d is %f'%(a,b,div))
print('Floored Quotient when %d is divided by %d is %d'%(a,b,floordiv))
print('Remainder when %d is divided by %d is %d'%(a,b,rem))
print('%d to the power of %d is %d'%(a,b,power))

