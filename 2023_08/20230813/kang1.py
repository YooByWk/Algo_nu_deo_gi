t = int(input())
for tc in range(1, t+1):
    n,m = map(int, input().split())  # 배양판 크기
    sepo_pan = [list(map(int,input().split())) for _ in range(n)]
    dr = [0,1,0,-1]  # 델타
    dc = [1,0,-1,0]  # 델타
    value_error = 0  # 오류
    for r in range(n):  #
        for c in range(m):  #
            cepo_many = 0  #
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < n and 0 <= nc < m :
                    if sepo_pan[nr][nc] == 1 :
                        cepo_many = 1
            if cepo_many == 1:
                value_error = 1

    if value_error == 0 :
        print(f"#{tc} {1}")
    elif value_error > 0:
        print(f"#{tc} {0}")