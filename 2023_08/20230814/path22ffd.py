import sys
sys.stdin = open('input.txt', 'r')

def dfs(start):
    visited = [False] * N
    st = []
    st.append(start)
    visited[start] = True
    while st:
        v = st.pop()
        if v == 99:
            return 1
        for w in G[v]:
            if not visited[w]:
                st.append(w)
                visited[w] = True
    else:
        return 0



for _ in range(10):
    t, E = map(int,input().split())
    lst = list(map(int, input().split()))

    N = 100
    # print(lst)
    G = [[] for _ in range(N)]
    for i in range(0, len(lst), 2):
        v1 = lst[i]
        v2 = lst[i+1]
        G[v1].append(v2)
    print(f'#{t} {dfs(0)}')

