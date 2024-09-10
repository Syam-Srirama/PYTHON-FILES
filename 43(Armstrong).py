import math
def armstrong (n):
    dc=0
    t=n
    while t:
        r=t%10
        dc=dc+1
        t=t//10

    sum=0
    t=n

    while n>0:
        r=n%10
        sum=sum+int(math.pow(r,dc))
        n=n//10

    if t==sum:
        return 1
    else:
        return 0

a,b=map(int,input().split())
for i in range (a,b,1):
    if (armstrong(i)): #if i ---> 1 or true
        print(i,end=" ")
print()
