def dfs(gp, start):
    visit = [False] * (V+1)
    st = []
    visit[0] = True
    st.append(start)
    while st:
        v = st.pop()
        if not visit[v]:
            # print(v)
            visit[v] = True
            if v == arv:
                return 1
        for w in G[v]:
            if not visit[w]:
                st.append(w)

    else:
        return 0
# 이 위를 잘 이해해보자.
T = int(input())
for t in range(1,T+1):
    V, E = map(int, input().split()) # v 수
    st = [] # 스택
    nd = [list(map(int, input().split())) for _ in range(E)] # 숫자 받기
    dep, arv = map(int, input().split()) #출발, 도착
    G =[[] for _ in range(V+1)]
    # print(nd)
    # print(G)
    for i in range(0,E):
        for idx in range(1):
            v1 = nd[i][idx]
            v2 = nd[i][idx+1]
            G[v1].append(v2)
            # G[v2].append(v1) #단방향임 ㅗ
    # print(G)
    KKK = dfs(G, dep)
    print(f'#{t} {KKK}')
