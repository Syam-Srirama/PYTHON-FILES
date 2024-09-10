n=int(input())
lst=list(map(int,input().split()))
for i in range(n):
    print(i,"---->",lst[i],end="\n")
print()
for i in lst:
    print(i,end=" ")
