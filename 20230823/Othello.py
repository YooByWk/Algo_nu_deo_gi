T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    BRD = [[0] * N for _ in range(N)]
    BRD[N // 2 - 1][N // 2 - 1] = 2
    BRD[N // 2][N // 2] = 2
    BRD[N // 2][N // 2 - 1] = 1
    BRD[N // 2 - 1][N // 2] = 1

    # print(BRD)
    for _ in range(M):
        C, R, color = map(int, input().split())
        C -= 1
        R -= 1
        BRD[R][C] = color
        if color == 2:
            revers_c = 1
        else:
            revers_c = 2

        for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            newR = R + dr
            newC = C + dc

            while 0 <= newR < N and 0 <= newC < N and BRD[newR][newC] == revers_c:
                newR += dr
                newC += dc

            if 0 <= newR < N and 0 <= newC < N and BRD[newR][newC] == color:
                # while BRD[newR][newC] == color:
                while newR != R or newC != C:
                    newR -= dr
                    newC -= dc
                    BRD[newR][newC] = color

    sum1 = 0
    sum2 = 0
    for r in range(N):
        sum1 += BRD[r].count(1)
        sum2 += BRD[r].count(2)
    print(f'#{tc}', sum1, sum2)