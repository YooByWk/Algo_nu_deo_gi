T = int(input())
for t in range(1, T+1):
    N = int(input()) # 색칠할 영역의 수
    lista1 = [[0] * 10 for _ in range(10)]
    # print(lista1)
    for i in range(N):
        r1, c1, r2, c2, colour = map(int, input().split())
        # print( r1,r2,c1,c2,colour)
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                lista1[r][c] += colour
    cnt = 0
    for r in range(10):
        for c in range(10):
            if lista1[r][c] == 3:
                cnt += 1
    print(f'#{t} {cnt}')