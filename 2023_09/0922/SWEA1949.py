# 등산로는 정점에서만 시작된다.
# 높은 곳에서 낮은 곳으로 가는 것이 등산로. 가로 또는 세로 델다
# 높이가 같아도 안됨
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def summit(x):
    Maxalt = x
    for r in range(N):
        for c in range(N):
            curalt = mt[r][c]
            if Maxalt < curalt:
                Maxalt = curalt

    return Maxalt


def summit_loc(alt):
    a = alt
    for r in range(N):
        for c in range(N):
            if mt[r][c] == a:
                tops.append((r, c))


def dfs(r, c, k, way):
    global Max_path
    # print(way)
    # if visit[r][c] == 1:
    #     return

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if nr < 0 or nr >= N or nc < 0 or nc >= N :
            continue

        if k == 0:
            if mt[nr][nc] >= mt[r][c] and visit[nr][nc] == 0:
                if way > Max_path:
                    Max_path = way
                    return

    # 기저조건
    # if k == 0 and   # 기준 조건보다 더 많이 까버린 경우, 컷
    #     return


    # 호출
    # for d in range(4):
    #     nr = r + dr[d]
    #     nc = c + dc[d]
        # 범위 못나가게 막음
        # if nr < 0 or nr >= N or nc < 0 or nc >= N:
        #     continue
        # 범위 내라면
        # 높이를 확인해야 한다. 무조건 작아야 한다.
        # 일단 낮은곳이라면
        if mt[nr][nc] < mt[r][c] and visit[nr][nc] == 0:
            visit[nr][nc] = 1
            dfs(nr, nc, k, way + 1)
            visit[nr][nc] = 0

        elif k > 0 and visit[nr][nc]== 0:  # 더 높은곳이라면.
            # 삽질 안헀을 때
            memo_alt = mt[nr][nc]
            while k != 0:
                mt[nr][nc] -= 1
                k -= 1
                if mt[nr][nc] < mt[r][c] and visit[nr][nc] == 0:
                    visit[nr][nc] = 1
                    dfs(nr, nc, 0, way + 1)
                    visit[nr][nc] = 0
                    mt[nr][nc] = memo_alt
            # else:
            #     return #  while 끝났고, 더 못파는데 넘어갈수도 없다? 넌 나가라.
        # else: # 여기까지 내려오는 근성이면
        #     return # 그냥 나가세요.
    # 행동


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    mt = [list(map(int, input().split())) for _ in range(N)]
    tops = []
    summit_loc(summit(0))
    visit = [[0] * N for _ in range(N)]
    # print(visit)
    Max_path = 0
    for row, col in tops:
        # print(row, col)
        shovel = False
        visit[row][col] = 1
        dfs(row, col, K, 1)
        visit[row][col] = 0
    print(f'#{tc} {Max_path}')
