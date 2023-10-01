# 5097 회전
# 빙글빙글빙글빙글빙글빙글
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    gira = 0
    Q = list(map(int, input().split()))
    while gira != M:
        gira += 1
        k = Q.pop(0)
        Q.append(k)
    else: print(f'#{t} {Q[0]}')
