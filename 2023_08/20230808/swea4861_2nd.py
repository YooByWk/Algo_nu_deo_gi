T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split()) #  m이 회문의 글자수
    lista = [input() for _ in range(N)] # input().split() 이런거 하지 말자. map 도 쓰지 말자
    # print((lista))
    for i in range(N-M+1):
        for r in range(N):
            tempR = ''
            # tempC = ''
            for c in range(i,i+M):
                # print(lista[r][c])
                tempR += lista[r][c]
                # tempC += lista[c][r]
            if tempR == tempR[::-1]:
                palin = tempR

        for c in range(N):
            tempC = ''
            for r in range(i,i+M):
                tempC += lista[r][c]
            if tempC == tempC[::-1]:
                palin = tempC
            # R = list(tempR)
            # for j in range(len(tempR) // 2):  # 뭐 [::-1] 쓰면 편하겠다만..
            #     R[j], R[len(R) - j - 1] = R[len(R) - j - 1], R[j]
            # RR = ''.join(R)
            # if tempR == RR:
            #     palin += RR
            # if tempR == tempR[::-1]:
            #     palin = tempR

            # C = list(tempC)
            # for k in range(len(tempC) // 2):
            #     C[k], C[len(C)-k-1] = C[len(C)-k-1], C[k]
            # CC = ''.join(C)
            # if tempC == CC:
            #     palin += CC
            # if tempC == tempC[::-1]:
            #     palin = tempC
    print(f'#{t} {palin}')





# tempR = 'abcde'
# R = list(tempR)
# for j in range(len(tempR)//2):
#     R[j], R[len(R) - j - 1] = R[len(R) - j - 1], R[j]
# K = ''.join(R)
# print(K == tempR[::-1])
