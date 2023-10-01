T = int(input())
for t in range(1,T+1):
    res = 0
    N = int(input())
    prices = list(map(int, input().split()))
    # p = s, N-1 지점 사이 max 의 위치
    # buy = s~p-1 의 합
    # sell = (p-s) *price[p]
    # s = p+1
    # 이득?
    CM = prices[N-1]
    for idx in range(N-2,-1, -1): # 뒤에서부터
        if CM > prices[idx]: # 작다면
            res += CM - prices[idx] # 더하고 합계에
        else:
            CM = prices[idx] # 아니라면 최대 갱신
    print(f'#{t} {res}')
