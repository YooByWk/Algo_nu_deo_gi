# 단방향 도로
from collections import deque
import sys
input = sys.stdin.readline

def bfs(X):
    visited = [0] * (N+1)
    q = deque([X])
    ans = []
    # q.append(X)  # X는 출발 위치다
    visited[X] = 1
    while q:
        tmp = q.popleft()
        if visited[tmp]+2 > K:
            ans.sort()
            return ans
        for t in near[tmp]:
            if visited[t] == 0 :
                q.append(t)
                visited[t] = visited[tmp] + 1
                if visited[t] -1 == K:
                    ans.append(t)
                elif visited[t] > K:
                    ans.sort()
                    return ans
                # if visited[t] > K + 1:
                #     break
    ans.sort()
    return ans


N, M, K, X = map(int,input().split())  # 도시 수, 도로 개수 ,거리 정보, 출발 번호
# 최단거리가 정확히 K인 장소만을 찾아라.
lst = []
for i in range(M):
    k = list(map(int,input().split()))
    lst.append(k)
# print(lst)
near = [[] for _ in range(N+1)]
# print(near)
for i in lst:
    a,b = i
    near[a].append(b)
# print(near)
if len(bfs(X)) == 0:
    print(-1)
else:
    aa = bfs(X).sort()
    for i in a:
        print(i, end='\n')