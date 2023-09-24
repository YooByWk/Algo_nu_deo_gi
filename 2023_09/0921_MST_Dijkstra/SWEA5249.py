# 5249. [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리 D3
#  V 번 까지 노드, E개의 간선을 가지는 그래프
# 이 그래프의 최소신장트리를 구성하라
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x,y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = []
    for _ in range(E):
        f, t, w = map(int, input().split())
        edge.append([f,t,w])
    edge.sort(key=lambda x: x[2])
    # print(edge)
    parent = [i for i in range(V+1)]
    # print(parent)
    cnt, _sum = 0, 0
    for f, t, w in edge:
        if find(f) != find(t):
            cnt += 1
            _sum += w
            union(f, t)
            if cnt == V:
                break
    print(f'#{tc} {_sum}')
