INF = 1e9
T = int(input())
for tc in range(1,T+1):
    N, M, X = map(int, input().split())

    cost = [[INF] * (N+1) for _ in range(N+1)]
    for i in range(N+1):
        cost[i][i] = 0
    for _ in range(M):
        f,t,w = map(int, input().split())
        cost[f][t] = w

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])
    _max = 0
    for i in range(1, 1+N):
        _max = max(_max, cost[i][X]+cost[X][i])
    print(f'#{tc} {_max}')

'''

10        
5 1       
9 3 2 3 2 
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
3 2       
1 2 1     
2 1 2
1 2 1
'''