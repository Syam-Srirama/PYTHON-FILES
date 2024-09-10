'''
lst1=[1,2,3,4,5]
lst2=lst1.copy()
#lst2=copy.copy(lst1)
print(lst1)
print(lst2)
print(lst1 is lst2)
print(id(lst1))
print(id(lst2))
lst1[1]=999
print(lst1)
print(lst2)
'''
print("SHALLOW COPY")
import copy
lst3=[11,22,33,[111,222,333],44,55]
lst4=copy.copy(lst3)
print(lst3)
print(lst4)
print(lst3 is lst4)
print(id(lst3))
print(id(lst4))
lst3[3][1]=999
print(lst3)
print(lst4)
print("DEEP COPY")
import copy
lst3=[11,22,33,[111,222,333],44,55]
lst4=copy.deepcopy(lst3)
print(lst3)
print(lst4)
print(lst3 is lst4)
print(id(lst3))
print(id(lst4))
lst3[3][1]=999
print(lst3)
print(lst4)


