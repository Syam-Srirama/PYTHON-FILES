import math
print("="*50)
print("ARITHEMATIC OPERATIONS")
print("="*50)
print("\t1.Addition")
print("\t2.Subtraction")
print("\t3.Division")
print("\t4.Multiplication")
print("\t5.Floored Division")
print("\t6.Remainder")
print("\t7.power")
print("="*50)

a,b=map(int,input("Enter a,b values:").split())
choice=int(input("Enter the operation you want toperform"))
match(choice):
    case 1:
        add=a+b
        print('The sum of {} and {} is {}'.format(a,b,add))
    case 2:
        sub=a-b
        print('The difference between {} and {} is {}'.format(a,b,sub))
    case 3:
        div=a/b
        print('The Quotient of {} and {} is {}'.format(a,b,div))
    case 4:
        mul=a*b
        print('The Multiplication of {} and {} is {}'.format(a,b,mul))
    case 5:
        floor=a//b
        print('The Floored Quotient of {} and {} is {}'.format(a,b,floor))
    case 6:
        Rem=a%b
        print('The Remainder of {} and {} is {}'.format(a,b,Rem))
    case 7:
        Power=math.pow(a,b)
        print('{} to the power of {} is {}'.format(a,b,Power))
    case _:
        print("Invalid Input")
