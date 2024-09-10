def primecheck2(n):
    for i in range(2,n):
        if n%i==0:
          return 0
    else:
        return 1

n=int(input("Enter a number:"))
result2=primecheck2(n)
if result2==1:
    print("{} is a prime number".format(n))
else:
    print("{} is not a prime number".format(n))
