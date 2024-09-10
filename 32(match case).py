import math
print("="*50)
print("\tArea:")
print("="*50)
print("\t1.Circle")
print("\t2.Rectangle")
print("\t3.Triangle")
print("\t4.Square")
print("="*50)
choice=int(input("Enter the operation you want toperform"))
match(choice):
    case 1:
        rad=int(input("Enter the radius of the circle:"))
        areac=math.pi*rad*rad
        print('The area of the circle with radius {} is {}'.format(rad,areac))
    case 2:
        leng,wid=map(int,input("Enter the length and width of the rectangle").split())
        arear=leng*wid
        print('The area of the rectangle with length:{} and width:{} is {}'.format(leng,wid,arear))
    case 3:
        base,hei=map(int,input("Enter the base and height of the triangle").split())
        areat=(1/2)*base*hei
        print('The area of the triangle with base:{} and Height:{} is {}'.format(base,hei,areat))
    case 4:
        side=int(input("Enter the side of the square"))
        areas=side*side
        print('The Area of the square with side:{} is {}'.format(side,areas))
    case _:
        print("Invalid Input")
