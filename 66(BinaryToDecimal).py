n=int(input())
decimal=0
power=1
while n!=0:
    r=n%10
    n=n//10
    decimal=decimal+r*power
    power=power*2
print(decimal)
