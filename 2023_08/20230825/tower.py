# 기지국

T = int(input())
for t in range(1,T+1):
    N = int(input())
    lst = [list(input())for _ in range(N+1)]
    # H 는 집  A B C 는 기지국
    dr = [0,0,-1,1]
    dc = [-1,1,0,0]
    A = 1
    B = 2
    C = 3
    for r in range(N+1):
        for c in range(N):
            if lst[r][c] == 'A':
                # print('AAAAAAAAAAA')
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0<= nr < N+1 and 0<= nc < N:
                        lst[nr][nc] = 'X'
            elif lst[r][c] == 'B':
                for i in range(4):
                    for j in range(B + 1):
                        nr = r + dr[i] * j
                        nc = c + dc[i] * j
                        if 0<= nr < N+1 and 0<= nc < N:
                            lst[nr][nc] = 'X'
            elif lst[r][c] == 'C':
                for i in range(4):
                    for j in range(C+1):
                        nr = r + dr[i] * j
                        nc = c + dc[i] * j
                        if 0<= nr < N+1 and 0<= nc < N:
                            lst[nr][nc] = 'X'
    ans = 0
    for i in range(N+1):
        ans += lst[i].count('H')
    print(f'#{t} {ans}')
