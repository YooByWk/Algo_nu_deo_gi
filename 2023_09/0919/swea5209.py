def comb(r,s):
    global _min
    # 조건
    if s > _min:
        return

    if r == N:
        if _min > s:
            _min = s
        return

    # 호출 + 할 일
    for i in range(N):
        if s < _min and not visit[i]:
            visit[i] = True
            comb(r+1,s+lst[r][i])
            visit[i] = False  # si s es menor que _min




T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    visit = [False] * N
    # print(visit)
# print(lst)
# en row 1 elige, una fabrica.
# luego solo faltan 2 cosas alla con la opcion con las que
# seleccionado
# entre combinacion, busca el minimo precio
    _min = 56781234789

    comb(0,0)
    print(f'#{t} {_min}')
# buen trabajo.
