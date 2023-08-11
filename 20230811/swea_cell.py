def isStable(r, c):
    Stable = 0
    if cell[r][c] == 1:
        for dr,dc in [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]:
            newR = r + dr
            newC = c + dc
            if (0 <= newR < N) and (0 <= newC < M):
                if cell[newR][newC] == 1:
                    Stable += 1

    return Stable


T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    # print(N,M)
    ss = 0
    cell = [list(map(int, input().split())) for _ in range(N)]
    for r in range(N):
        for c in range(M):
            ss += isStable(r,c)
    if ss == 0:
        print (f'#{t} 1')
    else:
        print(f'#{t} 0')
