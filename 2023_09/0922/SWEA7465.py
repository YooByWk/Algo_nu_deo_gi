# 창용 마을 무리의 개수

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])


def union(x,y):
    x = find(x)
    y = find(y)

    if x == y:
        # 사이클
        return

    if x < y:
        parent[y] = x
    else:
        parent[x] = y



T = int(input())
for tc in range(1,T+1):
    # 서로를 알고 있는 사람의 관계 수 를 구하라
    N , M = map(int, input().split())
    node = []
    parent = [i for i in range(N+1)]
    for _ in range(M):
        p1, p2 = map(int, input().split())
        union(parent[p1], parent[p2])
    ans = []
    for i in range(1,N+1):
        temp = find(i)
        ans.append(temp)
    print(f'#{tc} {len(set(ans))}')