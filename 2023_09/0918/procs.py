dx  = [1,-1,0,0]
dy  = [0,0,-1,1]
def dfs(corecheck,wire,core_cnt):
    global T_wire
    global T_core

    if core_cnt > T_core:
        T_wire = wire

    if core_cnt == stop: # 모든 코어 연결했다면,
        if core_cnt >= T_core:
            T_core = core_cnt
            if wire < T_wire:
                T_wire = wire

        return

    core_row, core_col = core_loc[corecheck]
    for d in range(4):
        nr = core_row
        nc = core_col
        route = []
        connec = []
        nr += dx[d]
        nc += dy[d]
        t_wire = 0
        while 0 < nr < N and 0 < nc < N and core[nr][nc] != 1:
            t_wire += 1
            core[nr][nc] = 1
            route.append((nr,nc))
            nr += dx[d]; nc += dy[d]
        else:
            if nr == 0 or nr == N or nc == 0 or nc >= N:
                # print(nr,nc)
                wire += t_wire
                # core_cnt += 1
                # connec.append(core_loc[corecheck])

                dfs(corecheck+1, wire, core_cnt+1)

                # 재귀는 초기화 해야한다.
                for i,j in route:
                    core[i][j] = 0


T = int(input())
for t in range(1,T+1):
    N = int(input())
    core = [list(map(int, input().split()))for _ in range(N)]
    # print(core)
    T_wire = 456745674567130
    T_core = 0
    # route = []
    core_loc = []
    for r in range(1,N-1):
        for c in range(1,N-1): # 1부터 시작하는 이유는 그냥 거기는 안볼것임
            # 같은 줄에 일단 코어가 있는지 확인합시다
            # 현재 자리 기준에서 4방향 내에 있으면 컷.
            if core[r][c] == 1:
                core_loc.append((r,c))
    stop = len(core_loc)
    print(core_loc)
    dfs(0,0,0)
    print(f'#{t} {T_wire}')
            # 없다면 0 개수 파악
