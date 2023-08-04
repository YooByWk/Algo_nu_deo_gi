T = int(input())
for t in range(1, 1+T):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    E = 'R'
    p = 1
    # print(snail)
    # se mueve  R D L U
    dr = [1 , -1, 0, 0] #상 하 좌 우
    dc = [0 , 0, -1, 1]
    ur = 0 # donde "snail" esta
    uc = 0 # donde "snail" esta
    # for r in range(N): # para
    #     for c in range(N): # moverlo
    for _ in range(N*N):
        snail[ur][uc] = p
        p += 1
        if E == 'R':
            if uc+1 < N and snail[ur][uc+1] == 0:
                uc += 1
            else:
                ur += 1
                E = 'D'
        elif E == 'D':
            if ur+1 < N and snail[ur+1][uc]== 0:
                ur += 1
            else:
                uc -= 1
                E = 'L'
        elif E == 'L':
            if uc > 0 and snail[ur][uc-1] == 0:
                uc -= 1
            else:
                ur -= 1
                E = 'U'

        elif E == 'U':
            if ur > 0 and snail[ur-1][uc]==0:
                ur -= 1
            else:
                uc += 1
                E = 'R'
    print(f'#{t}')
    for asd in snail:
        print(*asd)




