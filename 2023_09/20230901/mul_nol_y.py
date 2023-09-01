# 어떤 물인 칸으로 이동하기 위한 최소 이동 횟수
# W 에서 탐색을 해본다.
from collections import deque

T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    mapa = [input() for _ in range(N)]
    res = 0
    q = deque()
    vst= [[0]*M for _ in range(N)]
    # print(vst)
    for r in range(N):
        for c in range(M):
            if mapa[r][c] == 'W':
                # 여기서부터 탐색 해보는거죠 뭐
                q.append((r,c))
                vst[r][c] =0

    while q:
        ar,ac = q.popleft()
        for dr,dc in ((1,0),(-1,0),(0,-1),(0,1)):
            nr = ar + dr
            nc = ac + dc
            if 0<= nr < N and 0<= nc < M and vst[nr][nc] == 0 and mapa[nr][nc] == 'L' :
                vst[nr][nc] = 1 + vst[ar][ac]
                res += vst[nr][nc]
                q.append((nr,nc))
    print(f'#{t} {res}')
