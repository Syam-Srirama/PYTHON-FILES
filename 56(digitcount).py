import math
def digitcount(n):
    dc=0
    while n>0:
        r=n%10
        dc+=1
        n//=10
    return dc

n=int(input("Enter the number:"))
dc1=int(math.log10(n))+1
print("{} is the digit count by regular method.".format(dc1))
res=digitcount(n)
print("{} is the digit count by log10 method.".format(res))


