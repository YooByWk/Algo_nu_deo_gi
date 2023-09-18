    #
    #
    # if sum(res)> B and sum(res) < min:
    #     min = sum(res)

T = int(input())
for t in range(1,T+1):
    N,B = map(int, input().split())
    # B 는 최저 높이 / S 는 직원 총 합
    worker = list(map(int,input().split()))
    min = 139087891
    for i in range(1<<N):
        li = []
        for j in range(N):
            if i & (1<<j):
                li.append(worker[j])
        if sum(li)> B and sum(li) < min:
            min = sum(li)
    print(f"#{t} {min-B}")