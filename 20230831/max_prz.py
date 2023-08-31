def solve(k, s):
    global maxV
    if k == cnt:
        if maxV < int(s):
            maxV = int(s)
        return

    if s in memo[k]: # 백트레킹
        return
    else:
        memo[k].append(s)

        templst = list(s) # 임시임
        for i in range(N - 1):         # 조합 만들기
            for j in range(i + 1, N): # 조합 만들기
                templst[i], templst[j] = templst[j], templst[i]
                solve(k + 1, ''.join(templst))
                templst[i], templst[j] = templst[j], templst[i]


T = int(input())
for tc in range(1, T + 1):
    s, c = input().split()
    cnt = int(c)
    N = len(s)
    maxV = 0
    memo = [[] for _ in range(cnt)]
    solve(0, s)
    print(f'#{tc}', maxV)