t = int(input())
for tc in range(1,t+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    dr = [0, 1, 0, -1] #
    dc = [1, 0, -1, 0] #
    dia_r = [-1, 1, 1, -1] # X
    dia_c = [1, 1, -1, -1] # X
    max_sum1 = 0
    max_sum2 = 0
    maxx = 0
    for r in range(n): #
        for c in range(n):
            num_sum1 = arr[r][c]
            for l in range(1,m):
                for k in range(4):
                    nr = r + dr[k] * l
                    nc = c + dc[k] * l
                    if 0 <= nr < n and 0 <= nc < n:
                        num_sum1 += arr[nr][nc]
            if num_sum1 > max_sum1:
                max_sum1 = num_sum1
    for r in range(n):
        for c in range(n):
            num_sum2 = arr[r][c]
            for l in range(1,m):
                for k in range(4):
                    d_nr = r + dia_r[k] * l
                    d_nc = c + dia_c[k] * l
                    if 0 <= d_nr < n and 0 <= d_nc < n :
                        num_sum2 += arr[d_nr][d_nc]
            if num_sum2 > max_sum2:
                max_sum2 = num_sum2
    if max_sum1 < max_sum2:
        maxx = max_sum2
    else:
        maxx = max_sum1
    print(f"#{tc} {maxx}")