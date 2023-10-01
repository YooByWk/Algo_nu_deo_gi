def paper(Num):
    dp = [0] * (Num // 10 +1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 3
    for i in range(3, Num//10 + 1 ):
        dp[i] = dp[i-1] + (2 * dp[i-2])
    return dp[Num//10]


T = int(input())
for t in range(1, 1+T):
    N = int(input()) # N은 10의 배수라고 한다. . .
    print(f'#{t} {paper(N)}')
    # print(N // 10)
    # print()
