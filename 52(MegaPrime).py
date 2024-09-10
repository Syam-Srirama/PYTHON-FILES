def primecheck2(n):
    for i in range(2,n):
        if n%i==0:
          return 0
    else:
        return 1

def megaprime(n):
    while primecheck2(n): 
       dig=n%10
       n//=10
       if primecheck2(dig):
           return 1
       else:
           return 0

n=int(input())
res=megaprime(n)
if res==1:
    print("Mega Prime")
else:
    print("Not Mega Prime")
