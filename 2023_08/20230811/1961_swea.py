T = int(input())
for t in range(1,T+1):
    N = int(input())
    st = [list(input().split()) for _ in range(N)]
    # print((st))
    A = []
    B = []
    C = []
    for c in range(N):
        temp = ''
        for r in range(N-1,-1,-1):
            temp += st[r][c]
        A.append(temp)
    # print(A)
    for r in range(N-1, -1, -1):
        temp = ''
        for c in range(N-1, -1, -1):
            temp += st[r][c]
        B.append(temp)
    # print(B,'B')
    for c in range(N-1, -1, -1):
        temp = ''
        for r in range(N):
            temp += st[r][c]
        C.append(temp)
    # print(C)
    # print("----------------")
    print(f'#{t}')
    for i in range(N):
        print(f'{A[i]} {B[i]} {C[i]}')