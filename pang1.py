T = int(input())
N, M = map(int, input().split())
lista = []
for i in range(N):
    a = list(map(int, input().split())) #근데 리스트는 만들었어요
    lista.append(a) # 저는 이걸 이쁘게 받는 방법을 모르겠습니다.
    print(lista)
    # maximo = 0
    # for r in range(N):
    #     s = 0
    #     for c in range(M):
    #         n = lista[r][c]
    #         s += n
    #         dr = [n, -n, 0, 0]
    #         dc = [0, 0, -n, n]
    #         for i in range(4):
    #             # 실험
    #             # dr = [n, -n, 0, 0]
    #             # dc = [0, 0, -n, n]
    #             nr = r + dr[i]
    #             nc = c + dc[i]
    #             print(nr, nc)
    #             if 0 <= nr < N and 0 <= nc < M:
    #                 s += lista[nr][nc]1
    #
    #         if s < maximo :
    #             s = maximo


            # for d in range(4):
            #     nR = r + direccion_R[d]
            #     nC = c + direccion_C[d]
            #     if 0<=nR<N and 0 <= nC<N:
            #         s += lista[nR][nC]
            # if s < maximo :
            #     s = maximo
    # print(maximo)