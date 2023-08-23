import pprint


def tank():
    estado = '^v<>'
    for r in range(H):
        for c in range(W):
            if stage[r][c] in estado:
                head = stage[r][c]
                return head
def loc():
    for r in range(H):
        for c in range(W):
            if stage[r][c] ==tank():
                return (r,c)

def move(ss):
    global cc
    global cr
    l = {
        'U':0,'D':1,'L':2,'R':3
    }
    stage[cr][cc] = '.'
    nr = cr + dr[l[ss]]
    nc = cc + dc[l[ss]]
    if 0 <= nr < H and 0 <= nc < W:
        if stage[nr][nc] == '.':
            cr,cc = nr,nc
            if l[ss] == 0:
                stage[cr][cc] = '^'
            elif l[ss] == 1:
                stage[cr][cc] = 'v'
            elif l[ss] == 2:
                stage[cr][cc] = '<'
            elif l[ss] == 3:
                stage[cr][cc] = '>'
            return (cr,cc)


def sht(ss,hd):
    global stage
    sr = cr
    sc = cc
    l = {
        '^': 0, 'v': 1, '<': 2, '>': 3}
    sr += dr[l[hd]]
    sc += dc[l[hd]]
    while 0<= sr < H and 0<= sc < W:

        if stage[sr][sc] == '*':
            stage[sr][sc] = '.'
        elif stage[sr][sc] == '#':
            return
        sr += dr[l[hd]]
        sc += dc[l[hd]]


T =int(input())
for t in range(1,T+1):
    H,W = map(int,input().split())
    # 게임 맵은 H * W
    stage = [list(input()) for _ in range(H)]
    # print(stage) # 확인
    # . 점 : 전차가 들어갈 수 있음
    # * 벽돌 벽 :
    # # 강철 벽
    # - 물 : 전차는 들어갈 수 없다
    # ^ 아래가 평지일 때 위를 바라봄
    # v 아래 평지, 아래를 바라봄
    # < 왼쪽 바라봄 아래 평지
    # > 오른쪽 바라봄 ( 아래 평지는 전차의 현 위치가 평지라는 것 같다.
    # 맵 내부에서만 움직인다.
    # 포탄은 벽돌/강철 * # 까지 날아간다. 벽돌벽은 깨진다.
    # 강철벽은 누구보다 단단하다.
    '''
    ['*', '*', '*', '.', '.', '.', '.']
    ['*', '-', '.', '.', '#', '*', '*']
    ['#', '<', '.', '*', '*', '*', '*']
    '''
    n_task = int(input())
    task = list(input())
    # task 를 q 처럼 써보자.
    dr =[-1,1,0,0] # 상 하
    dc =[0,0,-1,1] # 좌 우
    hd = tank() # 전차의 상태를 확인
    cr, cc = loc() # 현재 위치
    # print(cr,cc)
    # print(tank()) # 확인용
    while task:
        do = task.pop(0)
        if do == 'U' :
            move(do)
            hd = '^'
            # nr = cr + dr[0];nc=cc+dc[0]
            # if 0<= nr < H and 0<= nc < W:
            #     if stage[nr][nc] == '.':
            #         cr,cc = nr,nc # 위로 단순 이동
            # print(stage)
            # print(tank())
            # print(loc())
        elif do ==  'D':
            move(do)
            hd = 'v'
            # nr= cr + dr[1];nc=cc+dc[1]
            # if 0<= nr < H and 0<= nc < W:
            #     if stage[nr][nc] == '.':
            # print(stage)
            # print(tank())
            # print(loc())

        elif do ==  'L':
            move(do)
            hd = '<'
            # print(stage)
            # print(tank())
            # print(loc())

        elif do ==  'R':
            move(do)
            hd = '>'
            # print(stage)
            # print(tank())
            # print(loc())

        elif do ==  'S':
            sht(do,hd)
    stage[cr][cc] = hd
    print(f"#{t}",end =' ')


    print(''.join(stage))
'''
        if do == '.':

        elif do == '*':

        elif do == '#':

        elif do == '-':

        elif do == '^':

        elif do == 'v':

        elif do == '<':

        elif do == '>':
'''

