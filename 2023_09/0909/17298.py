N = int(input())
lst = list(map(int, input().split()))
for i in range(N-1):
    fixed = lst[i]
    check = lst[i:i+1]
    check.sort()
    print(lst[-1])
print(-1)
