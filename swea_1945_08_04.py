T = int(input())
for t in range(1, T+1):
    N = int(input())
    # 2, 3, 5, 7, 11
    lst = [0] * 5
    while N != 1: # 1 될 때 까 지
        if N % 2 == 0: # 2 로 나 눈 다
            N = N / 2
            lst[0] += 1
        elif N % 3 == 0: # 3 으 로 나 눈 다
            N = N / 3
            lst[1] += 1
        elif N % 5 == 0: # 5 로 나 눈 다
            N = N / 5
            lst[2] += 1
        elif N % 7 == 0: # 7 로 나 눈 다
            N = N / 7
            lst[3] += 1
        elif N % 11 == 0: # 11 로 나 눈 다
            N = N / 11
            lst[4] += 1
    print(f'#{t}', *lst)

