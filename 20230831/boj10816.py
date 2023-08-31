import sys
input = sys.stdin.readline
M = int(input())
# for i in range(M):
lst = list(map(int, input().split()))
N = int(input())
sang = list(map(int, input().split()))
for i in sang:
    print(lst.count(i), end =' ')