T = int(input())
for t in range(1,T+1):
    sett = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n, k = map(int, input().split())
    sub = 0
    for i in range(1 << 12):
        S = 0
        cnt = 0
        for j in range(12):
            if i & (1 << j):
                S += sett[j]
                cnt += 1 #원소 추가하면 cnt 1 증가
        # print(tlist)
        if cnt == n:
            if S == k : # k가 합
                sub += 1 #

    print(f'#{t} {sub}')
    # 공사중