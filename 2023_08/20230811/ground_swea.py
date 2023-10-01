def getMaxCnt(r, c):
    cnt = 0
    for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        newR = r + dr
        newC = c + dc
        if 0 <= newR < N and 0 <= newC < M:
            if arr[newR][newC] > arr[r][c]:
                cnt += 1

    return cnt

T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    # print(N,M)
    arr = [list(map(int, input().split())) for _ in range(N)]
    resCon = 0
    mas = 100 * N * M
    for r in range(N):
        for c in range(M):
            # print(arr[r][c], getMaxCnt(r, c))
            if getMaxCnt(r, c) == 4:

                resCon += 1
                # print(resCon)
                if mas > arr[r][c]:
                    mas = arr[r][c]
    if resCon == 0:
        mas = -1
    print(f'#{t} {resCon} {mas}')
