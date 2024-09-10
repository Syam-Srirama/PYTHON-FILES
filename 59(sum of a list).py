n = int(input())
lst = list(map(int, input().split()))
total_sum = 0
for i in range(n):
    total_sum += lst[i]
print(total_sum)
