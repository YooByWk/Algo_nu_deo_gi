def mmax(a,b):
    lst = (a,b)
    cur_max = 0
    for i in lst:
        if i > cur_max:
            cur_max = i
    return cur_max

T = 10
for t in range(1, T+1):
    a = int(input())
    N = 100
    lista = [list(map(int, input().split())) for _ in range(N)]
    #print(lista)
    sumax = 0
    for r in range(N):
        s1 = 0
        for c in range(N):
            s1 += lista[r][c]  # 가로로 달렷
        if sumax < s1:
            sumax = s1
    for c in range(N):
        s2 = 0
        for r in range(N):
            s2 += lista[r][c]
        if sumax < s2:
            sumax = s2
    s3 = 0
    s4 = 0
    for i in range(N):
        s3 += lista[i][i]
        s4 += lista[i][N-1-i]
        if sumax < mmax(s3,s4):
            sumax = mmax(s3,s4)
    print(f'#{t} {sumax}')