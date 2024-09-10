def primecheck2(n):
    if n==1:
        return 0
    for i in range(2,n):
        if n%i==0:
          return 0
    else:
        return 1

n=int(input("Enter a number:"))
n=n-1
while True:
    if (primecheck2(n)):
        print("The Previous prime number is {}".format(n))
        break
    n=n-1
