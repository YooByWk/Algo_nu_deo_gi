T = int(input())
for t in range(1,T+1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    v = 0 # 델타
    r = 0 # r
    c = 0 # c
    for row in range(1,N*N+1): # 달팽이의 숫자
        snail[r][c] = row # 그 자리에 넣어줍니다. 숫자를
        r += dr[v] # 이동
        c += dc[v] # 이동
        if r < 0 or c < 0 or r >= N or c >= N or snail[r][c] != 0: #나가지 말아라
            r -= dr[v]  # 나간 케이스니까
            c -= dc[v]  # 나간 케이스니까
            v = (v+1)%4 # 나간 케이스 / 우하좌상으로 델타 세워뒀음
            r += dr[v]  # 따라서 변한 델타값 적용
            c += dc[v]  # 여기도
    print(snail)


