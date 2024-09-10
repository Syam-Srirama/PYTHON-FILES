quantity=int(input("Enter the Quantity:"))
price=int(input("Enter the price:"))
amount=price*quantity
print("Your original bill is:{}".format(amount))
if quantity >= 100:
    amount=(amount*90)//100
    print("You got 10% discount on your bill!!")
print("Your final bill is:{}".format(amount))
