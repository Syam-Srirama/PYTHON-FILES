def primecheck2(n):
    if n<2:
        return 0
    for i in range(2,n):
        if n%i==0:
          return 0
    return 1
def fun(n):
    if primecheck2(n):
        print(n)
    else:
        lower = n - 1
        upper = n + 1
        while True:
            if primecheck2(lower):
                nearest_prime = lower
                break
            lower -= 1
        while True:
            if primecheck2(upper):
                nearest_prime = upper
                break
            upper += 1

        if n-lower<upper-n:
            print(lower)
        elif n-lower>upper-n:
            print(upper)
        elif n-lower==upper-n:
            print (min(lower,upper))

tc=int(input())
while tc>0:
    t=int(input())
    fun(t)
    tc=tc-1

