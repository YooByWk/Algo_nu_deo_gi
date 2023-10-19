# 탈주범 검거            # 탈주범 검거
            # 탈주범 검거
# 탈주범 검거            # 탈주범 검거
from collections import deque

def bfs(tr, tc):
    global cnt
    global time
    q = deque()
    vst = [[0]*M for _ in range(N)]
    q.append((tr,tc))
    vst[tr][tc] = 1
    while q:
        r,c = q.popleft()
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0<= nr < N and 0<= nc < M and vst[nr][nc] == 0 and tn[nr][nc] != 0:
                if connect(r,c,tn[r][c]) :
                    q.append((nr,nc))
                    vst[nr][nc] += vst[r][c] + 1
                    cnt += 1
        time += 1
        if time > L:
            return
def connect(r,c,num):
    dr = [r-1,r+1,r,r]
    dc = [c,c,c-1,c+1]
    # 0상 1하 2좌 3우
    if num == 1:
        if 0<= dr[0] < N and 0<= dc[0] < M :
            if tn[dr[0]][dr[0]] in D:
                return True
        if 0<= dr[1] < N and 0<= dc[1] < M :
            if tn[dr[1]][dr[1]] in U:
                return True
        if 0 <= dr[2] < N and 0 <= dc[2] < M:
            if tn[dr[2]][dr[2]] in Rht:
                return True
        if 0 <= dr[3] < N and 0 <= dc[3] < M:
            if tn[dr[3]][dr[3]] in Lft:
                return True
        return False
    elif num == 2:
        if 0<= dr[0] < N and 0<= dc[0] < M :
            if tn[dr[0]][dr[0]] in D:
                return True
        if 0 <= dr[1] < N and 0 <= dc[1] < M:
            if tn[dr[1]][dr[1]] in U:
                return True
    elif num == 3:
        if 0 <= dr[2] < N and 0 <= dc[2] < M:
            if tn[dr[2]][dc[2]] in Rht:
                return True
        if 0 <= dr[3] < N and 0 <= dc[3] < M:

            if tn[dr[3]][dc[3]] in Lft:
                return True
    elif num == 4:
        if 0<= dr[0] < N and 0<= dc[0] < M :

            if tn[dr[0]][dc[0]] in D:
                return True
        if 0 <= dr[3] < N and 0 <= dc[3] < M:

            if tn[dr[3]][dc[3]] in Lft:
                return True
    elif num == 5:
        if 0 <= dr[1] < N and 0 <= dc[1] < M:

            if tn[dr[1]][dr[1]] in U:
                return True
        if 0 <= dr[2] < N and 0 <= dc[2] < M:

            if tn[dr[2]][dr[2]] in Rht:
                return True

    elif num == 6:
        if 0 <= dr[1] < N and 0 <= dc[1] < M:

            if tn[dr[1]][dr[1]] in U:
                return True
        if 0 <= dr[2] < N and 0 <= dc[2] < M:

            if tn[dr[2]][dr[2]] in Rht:
                return True

    elif num == 7:
        if 0<= dr[0] < N and 0<= dc[0] < M :

            if tn[dr[0]][dr[0]] in D:
                return True
        if 0 <= dr[3] < N and 0 <= dc[3] < M:

            if tn[dr[3]][dr[3]] in Lft:
                return True



for t in range(1, int(input())+1):
    N,M,R,C,L = map(int,input().split())
    # 세로, 가로, 맨홀뚜껑세로, 맨.뚜 가로, 탈.소
    tn = [list(map(int,input().split()))for _ in range(N)]
    # 숫자 1 2 3 4 5 6 7 은 각 터널 구조물 0 은 터X
    # 상
    U = [1,2,4,7]
    # 하
    D = [1,2,5,6]
    # 좌
    Lft  = [1,3,6,7]
    # 우
    Rht = [1,3,4,5]
    time = 1
    cnt = 1
    bfs(R,C)
    print(cnt)
