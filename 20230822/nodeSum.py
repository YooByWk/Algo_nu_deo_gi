def pst(root):
    if root > N:
        return 0
    if tr[root]:
        return tr[root] # 값 있으면 탈출
    else:
        l = pst(root*2)
        r = pst(root*2+1)
        tr[root] = l + r
    return tr[root]

T = int(input())
for t in range(1,T+1):
    N, M ,L = map(int, input().split())
    # N : 노드 수, M 리프노드 수, L 값 출력 노드
    tr = [0] * (N+1)
    for i in range(M):
        # 리프 번호, 자연수
        nd, val = map(int, input().split())
        tr[nd] = val
    print(f"#{t} {pst(L)}")