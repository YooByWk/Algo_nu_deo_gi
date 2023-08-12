T = int(input())
for t in range(1, 1+T):
    N = int(input())
    num = [list(map(str, input().split()))for _ in range(N)]
    # print(num)
    A = []
    B = []
    C = []
    T = []
    # A
    for c in range(N):
        temp = []
        for r in range(N-1,-1,-1):
            temp.append(num[r][c])
        A.append(temp)
    # print(A)
    # B
    for r in range(N-1,-1,-1):
        temp = []
        for c in range(N-1,-1,-1):
            temp.append(num[r][c])
        B.append(temp)
    # print(B)
    # C
    for c in range(N-1,-1,-1):
        temp = []
        for r in range(N):
            temp.append(num[r][c])
        C.append(temp)
    # print(C)
    T.append(A)
    T.append(B)
    T.append(C)

    print(f'#{t}')
    helpme = []
    for a in range(3):
        rodong = ' '
        for b in range(N):
            temp = ''
            for c in range(N):
                temp += str(T[a][b][c])
            zebal = temp + rodong
            # print(zebal,end=' ')
            helpme.append(zebal)
    # print(helpme)
    # print('asdfhlasdkljhsdljkh')
    for i in range(len(helpme)//3):
        print(f'{helpme[i]}{helpme[i+3]}{helpme[i+6]}')