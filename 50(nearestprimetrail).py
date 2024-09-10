def primecheck2(n):
    if n<2:
        return 0
    for i in range(2,n):
        if n%i==0:
          return 0
    else:
        return 1

n=int(input("Enter a number:"))
t=n
n=n+1
while True:
    if (primecheck2(n)):
        np=n
        break
    n=n+1
n=t
n=n-1
while True:
    if (primecheck2(n)):
        pp=n
        break
    n=n-1






if np-n==n-pp:
    print(pp,np)
elif np-n>n-pp:
    print(pp)
else:
    print(np)
