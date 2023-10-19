from collections import deque

def bfs(mapa, start):
    N, M = len(mapa), len(mapa[0])
    visited = [[False] * M for _ in range(N)]
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True
    distance = 0

    while queue:
        size = len(queue)
        for _ in range(size):
            r, c = queue.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and mapa[nr][nc] == 'L':
                    visited[nr][nc] = True
                    distance += 1
                    queue.append((nr, nc))

    return distance

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    mapa = [list(input()) for _ in range(N)]
    total_distance = 0

    for r in range(N):
        for c in range(M):
            if mapa[r][c] == 'L':
                total_distance += bfs(mapa, (r, c))

    print(f'#{t} {total_distance}')
