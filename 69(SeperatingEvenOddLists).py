lst=[1,2,3,4,5,6,7,8,9,0]
even=[]
odd=[]
for i in lst:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
