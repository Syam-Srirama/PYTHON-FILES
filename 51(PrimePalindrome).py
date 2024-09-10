def palindrome(n):
    t=n
    rev=0
    while n>0:
      r=n%10
      rev=rev*10+r
      n=n//10
    if rev==t:
      return 1
    else:
      return 0
    
def primecheck2(n):
    for i in range(2,n):
        if n%i==0:
          return 0
    else:
        return 1

n=int(input())
if primecheck2(n) and palindrome(n):
    print("The given number is a prime palindrome")
else:
    print("The given number is not a prime palindrome")
