T = int(input())
for t in range(1,T+1):
    A, B = input().split()
    # print(A,B)
    M = len(A)
    N = len(B)
    ap = 0
    bp = 0
    cnt = 0
    # while ap < M:
    #     while ap<M and bp<N:
    #         if A[ap] != B[bp]:
    #             ap = ap - bp + 1
    #             bp = 0
    #         else:
    #             ap += 1
    #             bp += 1
    #     if bp == N: # 찾으면
    #         cnt += 1
    #         ap += 1
    #         bp = 0
    #     # print(ap, M) # 4, 6
    # times = M - (N*cnt) + cnt
    # # print(M,' 횟수')
    # # print(cnt)
    # print(f'#{t} {times}')
    # cnt = 0
    # for i in range(M): # 전체 문자
    #     v = 0
    #     for j in range(N):
    #         for k in range(j,j+N):
    #             if A[i+k] == B[j]:
    #                 v += 1
