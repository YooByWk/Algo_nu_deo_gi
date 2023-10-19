def comb(i,N,s):
    global ans
    if s > K:
        return

    if i == N:
        s = 0
        for j in range(N):
            if bit[j]:
                s += arr[j]
        if s == K:
            ans += 1

    else:
        bit[i] = 1
        comb(i+1, N,s+arr[i])
        bit[i] = 0
        comb(i+1, N,s)

T = int(input())
for t in range(1, T+1):
    N,K = map(int,input().split())
    arr = list(map(int,input().split()))
    bit = [0] * N
    ans = 0
    s = 0
    comb(0,N,s)
    print(f"#{t} {ans}")
