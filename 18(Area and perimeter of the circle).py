#Find The Area and perimeter of the Circle
# Area=𝜋𝑟^2
#perimeter=2𝜋𝑟
import math
rad=int(input("Enter the radius of the circle:\n"))
area=math.pi*rad*rad
perimeter=2*math.pi*rad
print('Area:{}'.format(area))
print('Perimeter:{}'.format(perimeter))
