# 5102 노드의 거리
# Bfs 연습
'''
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
'''
def bfs(S,G):
    visited = [-1] * (V+1)
    q =[]
    q.append(S)
    visited[S] = 0
    while q:
        t = q.pop(0)
        if t == G:
            return visited[t]
        else:
            for w in xkrptdlehlrhtlvdmsfltmxmdmldlfmadmswjdakfrlfdjdy[t]:
                if visited[w] == -1:
                    q.append(w)
                    visited[w] = visited[t] + 1
    return 0






T = int(input()) # 인?풋?
for t in range(1, 1+T):
    V, E = map(int, input().split())
    xkrptdlehlrhtlvdmsfltmxmdmldlfmadmswjdakfrlfdjdy = [[] for _ in range(V+1)]     # 인접 리스트 만들기
    for i in range(E): # 여기서 입력받아요
        v1, v2 = map(int, input().split())
        xkrptdlehlrhtlvdmsfltmxmdmldlfmadmswjdakfrlfdjdy[v1].append(v2) # 타겟이되고싶은리스트의이름은정말길어요
        xkrptdlehlrhtlvdmsfltmxmdmldlfmadmswjdakfrlfdjdy[v2].append(v1)
    # print(tg)
    S, G = map(int, input().split())
    esto_sera_la_clave_del_problema_creo_que_si_podria_ser = bfs(S,G)
    print(f'#{t} {esto_sera_la_clave_del_problema_creo_que_si_podria_ser}')
