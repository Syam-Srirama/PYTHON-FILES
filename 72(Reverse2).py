def revers(lst,s,e):
    while s<=e:
        lst[s],lst[e]=lst[e],lst[s]
        s=s+1
        e=e-1
    return lst


lst=[1,2,3,4,5]
print(revers(lst,0,len(lst)-1))
