a=int(input("Enter 1st Number:"))
b=int(input("Enter 2nd Number:"))
total=0


def primecheck2(n):
    if n==0:
        return 0
    for i in range(2,n):
        if n%i==0:
          return 0
    else:
        return 1



for i in range(a,b+1):
    if(primecheck2(i)):
        total+=1
        print(i,end=" ")
print()
print("There are a total of {} prime numbers in between {} and {}".format(total,a,b))


