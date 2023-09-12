#dfs and bfs
from collections import deque

def dfs(start):
    visited  = [False] * (N + 1)
    st = []
    st.append(start)
    while st:
        k = st.pop()
        if visited[k] == False:
            visited[k] = True






def bfs(start):
    # pass
    visited = [False] * (N + 1)

N,M,V = map(int, input().split())
# N 정점의 개수
# M 간선의 개수
# V 시작 지점
# print(N,M,V)
nd = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int,input().split())
    nd[a].append(b)
    nd[b].append(a)
print(nd)
# for i in nd:
#     i.sort(reverse=True)

dfs_nd = nd[:]
dfs_nd.sort(reverse=True)

dfs(V)

print()
bfs(V)
