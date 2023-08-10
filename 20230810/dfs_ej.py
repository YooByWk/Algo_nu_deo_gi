def dfs(s):
    ST = []
    visited = [False] * (N+1)
    ST.append(s)
    while ST:
        v = ST.pop()
        if not visited[v]:
            print(v)
            visited[v] = True
        for w in G[v]:
            if not visited[w]:
                ST.append(w)

def dfs1(s):
    # 지난 길을 넣거나
    # 갈림길을 넣거나.
    ST = [] # 스택 준비하기
    visited = [False] * (N+1)
    ST.append(s)
    visited[s] = True
    while ST:
        v = ST.pop()
        # if not visited[v]:
        print(v)
            # visited[v] = True
        for w in G[v]: # [2, 3] 들어오는데 2 3 한번씩
            if not visited[w]:
                ST.append(w)
                visited[w] = True
        # for d in range(4):"
        newX, newY = ...

N = 7
S = '1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7'
lst = list(map(int, S.split(',')))
#print(lst)
G = [[] for _ in range(N+1)]
for idx in range(0,len(lst), 2):
    v1 = lst[idx]
    v2 = lst[idx+1]
    G[v1].append(v2)
    G[v2].append(v1)

print(G)

dfs(1) # 1에서 dfs 시작
'''
G = [
    [],
    [2,3], # 1
    [1, 4, 5], # 2
    [1, 7], # 3
    [2, 6],
    [2, 6],
    [4, 5, 7],
    [3, 6]
]
'''
visited = [False] * (N + 1)
def dfs_recur(v):
    print(v)
    visited[v] = True
    for w in G[v]:
        if not visited[w]:
            dfs(w)