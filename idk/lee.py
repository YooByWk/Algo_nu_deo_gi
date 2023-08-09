def bsearch(fi, num):
    start = 1
    end = fi
    cnt = 0
    while start <= end:
        cnt += 1
        c  = (start + end) // 2
        if c == num:
            return cnt
        if c < num:
            start = c
        if c > num:
            end = c
    return 0

T = int(input())
for t in range(1, T+1):
    l, pa, pb = map(int, input().split())
    A = bsearch(l, pa)
    # print(A, 'a')
    B = bsearch(l, pb)
    # print(B, 'b')
    if A < B:
        print(f'#{t} A')
    elif A == B:
        print(f'#{t} 0')
    else:
        print(f'#{t} B')