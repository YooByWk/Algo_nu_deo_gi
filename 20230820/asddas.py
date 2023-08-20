from collections import deque
import sys
input = sys.stdin.readline
def bfs(X):
    visited = [0] * (N + 1)
    q = deque([X])
    ans = []
    visited[X] = 1
    unvisited = N

    while q:
        tmp = q.popleft()
        for t in near[tmp]:
            if visited[t] == 0:
                q.append(t)
                visited[t] = visited[tmp] + 1
                unvisited -= 1

                if visited[t] - 1 == K:
                    ans.append(t)

                if visited[t] > K:
                    return ans

    return ans

N, M, K, X = map(int, input().split())
lst = []

for i in range(M):
    k = list(map(int, input().split()))
    lst.append(k)

near = [[] for _ in range(N + 1)]

for i in lst:
    a, b = i
    near[a].append(b)

result = bfs(X)

if len(result) == 0:
    print(-1)
else:
    result.sort()  # Sort the result in ascending order.
    for i in result:
        print(i)
