import sys
input = sys.stdin.readline

N = int(input())
ans = []
for i in range(N):
    ans.append(int(input()))
ans.sort(reverse=False)
for i in ans:
    print(i)