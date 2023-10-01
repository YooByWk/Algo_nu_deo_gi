T = int(input())
for t in range(1,T+1):
    A, B = input().split()
    # print(A,B)
    M = len(A)
    N = len(B)
    ap = 0
    bp = 0
    cnt = 0
    cc = A.count(B)
    print(cc)
    times = M - (N*cnt) + cnt
    # print(M,' 횟수')
    # print(cnt)
    print(f'#{t} {times}')