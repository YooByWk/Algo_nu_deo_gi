
T = int(input())
for t in range(1, T+1):
    ###########
    N, M = map(int,(input().split()))
    lista = [list(map(int, input().split())) for _ in range(N)]
    # print(lista)
    suma = 0

    for i in range(N-M+1): # 가로로 가는데 암튼 이만큼 감
        for j in range(N-M+1): # #니는 세로
            s = 0
            for r in range(i, i+M): #  파리채 |
                for c in range(j, j+M): # 파리채 ㅡ
                    s += lista[r][c]

            if suma < s:
                suma = s
    print(f'#{t} {suma}')
