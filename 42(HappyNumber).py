num=int(input("Enter a Number:"))
seen=set()
while num not in (1,7) and num not in seen:
    seen.add(num)
    total=0
    digit=num%10
    total+=digit*digit
    num//=10
    num=total
if num in (1,7):
    print(True)
else:
    print(False)
