'''
주서크

'''
T = int(input())
for tc in range(1, T+1):
    t, p = input().split()
    N = len(t)
    M = len(p)

    tp = 0
    pp = 0
    while True:
        if t[t] != p[pp]:
            tp = tp -pp+1
            pp= 0
        else:
            tp += 1
            pp += 1
            if pp= M:
                cnt += 1
                pp = 0
    print(f'# {tc} {M - (N*cnt) + cnt} ')