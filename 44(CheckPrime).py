def primecheck(m):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    if fc==2:
        return 1
    else:
        return 0


n=int(input("Enter a number:"))
result=primecheck(n)
result2=primecheck2(n)
if result==1:
    print("{} is a prime number".format(n))
else:
    print("{} is not a prime number".format(n))
