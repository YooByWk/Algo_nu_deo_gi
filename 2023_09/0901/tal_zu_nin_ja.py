Delta = [(-1,0), (1,0), (0,-1), (0,1)]
pp = [[0,0,0,0],[1,1,1,1], [1,1,0,0],[0,0,1,1],
      [1,0,0,1], [0,1,0,1],[0,1,1,0],[1,0,1,0]]
opp = [1,0,3,2]

def bfs(r,c):
    visited = [[False]*M for _ in range(N)]
    Q = [(r,c,1)]
    visited[r][c] = True
    while Q:
        r, c, t = Q.pop(0)

        if t >= L:
            break
        for d in range(4):
            nr = r+ Delta[d][0]
            nc = c+ Delta[d][1]
            if 0<=nr<N and 0<=nc<M and not visited[nr][nc]:
                p1 = tn[r][c]
                p2 = tn[nr][nc]
                if pp[p1][d] and pp[p2][opp[d]]:
                    Q. append((nr,nc,t+1))
                    visited[nr][nc] = True
    res = 0
    for rst in visited:
        res += rst.count(True)
    return res


for t in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    # 세로, 가로, 맨홀뚜껑세로, 맨.뚜 가로, 탈.소
    tn = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t} {bfs(R, C)}')
