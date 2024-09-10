name=input("Enter the name of the student")
sub1=int(input("Enter the subject1 marks:"))
sub2=int(input("Enter the subject2 marks:"))
sub3=int(input("Enter the subject3 marks:"))
if sub1>=40 and sub2>=40 and sub3>=40:
    print('{} passed in the exam'.format(name))
else:
    print('{} failed in the exam'.format(name))
