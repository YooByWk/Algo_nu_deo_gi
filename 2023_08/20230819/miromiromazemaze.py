# s/w 문제해결 기본 7일차 미로2
# 행렬은 100 * 100
def startpoint():
    for r in range(100):
        for c in range(100):
            if maze[r][c] == 2:
                return r,c


def bfs(SR,SC):
    q = []
    visited = [[False]*100 for _ in range(100)]
    q.append((SR, SC))
    visited[SR][SC] = True
    while q:
        r, c = q.pop(0)
        if maze[r][c] == 3:
            return 1
        for dr, dc in [[0,1],[0,-1],[1,0],[-1,0]]:
            nr = r + dr
            nc = c + dc
            if 0<= nr<100 and 0<=nc<100 and visited[nr][nc] == 0 and maze[nr][nc] != 1 :
                q.append((nr,nc))
                visited[nr][nc] = 1
    return 0


for _ in range(1,11):
    t = int(input())
    maze = [list(map(int, input()))for _ in range(100)]
    # print(maze)
    sR, sC = startpoint()
    print(f'#{t} {bfs(sR,sC)}')
