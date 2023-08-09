T = int(input())
for t in range(1,1+T):
    N = int(input())
    cnt = 0
    for x in range(1,N):
        for y in range(1,N):
            if (x ** 2 + y ** 2) <= N**2:
                cnt += 1
    cnt = 4 * cnt +(4 * N) + 1
    print(f'#{t} {cnt}')

help(list.sort)