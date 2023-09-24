# swea 동철이의 일 분배
def wk(r,mul):
    global pst
    # 정지
    if mul <= pst:
        return
    # 작업
    if r == N:
        if pst < mul:
            pst = mul
        return

    # 호출
    for i in range(N):
        if not visit[i]:
            visit[i] = True
            wk(r+1, mul * lst[r][i] / 100)
            visit[i] = False

T = int(input())
for t in range(1,T+1):
    N = int(input()) # lineas de posiblidad
    # el numero empieza en 1 // trabajos tambien
    # 2 dimension
    lst = [list(map(int,input().split())) for _ in range(N)]
    # print(lst)
    pst = 0
    visit = [False] * N
    wk(0,1)
    pst *= 100
    print(f'#{t} {pst:0.6f}')