#6.find the Distance between two points
 # distance=sqrt((x2-x1)^2+(y2-y1)^2)
import math
print("Enter the coordinates of the first point:\n")
x1=int(input("Enter x cordinate"))
y1=int(input("Enter y cordinate"))
print("Enter the coordinates of the second point:\n")
x2=int(input("Enter x cordinate"))
y2=int(input("Enter y cordinate"))
Distance=math.sqrt(((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1)))
print(Distance)
