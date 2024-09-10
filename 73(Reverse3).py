def revers(lst,s,l):
    while s<=l:
        lst[s],lst[l]=lst[l],lst[s]
        s=s+1
        l=l+1
    return lst
lst=list(map(int,input().split()))
b=0
e=len(lst)-1
print(revers(lst,b,e))
