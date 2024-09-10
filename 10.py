import math
a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
d=int(input("Enter a number"))
a1=a%10
print('Last digit of %d is %d'%(a,a1))
b1=b%10
print('Last digit of %d is %d'%(b,b1))
c1=c%10
print('Last digit of %d is %d'%(c,c1))
d1=d%10
print('Last digit of %d is %d'%(d,d1))
result=a1*b1*c1*d1
print('Product of the last digits of the given four numbers is:{}'.format(result))
