n=int(input())
prev=-1
curr=1
for i in range(prev,n+1,1):
    next1=prev+curr
    prev=curr
    curr=next1
    print(next1,end=" ")


print()

n=int(input())
a=0
b=1
print(a,b,end=" ")
c=a+b
i=1
while i<=n-2:
    print(c,end=" ")
    a=b
    b=c
    c=a+b
    i=i+1
