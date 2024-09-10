unit=int(input("Enter the number of units consumed:"))
price=unit*1
if unit <= 199:
    price=unit*1.20
elif unit >199 and unit <400:
    price=unit*1.50
elif unit >400 and unit <600:
    price=unit*1.80
elif unit >=600:
  price=unit*2.00
total=price
if total>400:
    total=((total*15)/100)+total
print("Your total electricity bill is:{}".format(total))
    
