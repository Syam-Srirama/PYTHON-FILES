a=int(input("Enter the number of days"))
year=a//365
week=(a-(year*365))//7
day=(a-(year*365)-(week*7))
print('It is %d years,%d weeks and %d days'%(year,week,day))
 
