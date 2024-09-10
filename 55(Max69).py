import math
n=int(input("Enter the number:"))
dc=int(math.log10(n))
sum=0
flag=0
while n>0:
    r=n//math.ceil(10**dc)
    if flag==0:
        if r!=9:
            sum=sum*10+9
            flag=1
        else:
            sum=sum*10+r
    else:
        sum=sum*10+r
    n=int(n%math.ceil(10**dc))
    dc=dc-1
print("The maximum 69 number is:{}".format(int(sum)))
