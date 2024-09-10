n=int(input())
print(bin(n))
binary=0
power=1
while n!=0:
    r=n%2
    n=n//2
    binary=binary+r*power
    power=power*10
print(binary)

