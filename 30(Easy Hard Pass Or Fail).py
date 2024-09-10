easy=int(input("Enter the number of easy questions attempted:"))
hard=int(input("Enter the number of hard questions attempted:"))
points=(easy*1)+(hard*2)
req=int(input("Enter the minimum marks required to Qualify in the exam:"))
if points >= req:
    print("Student is Qualified for next round")
else:
    print("Student is Not Qualified for next round")

