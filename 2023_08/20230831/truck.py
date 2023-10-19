T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())        # 컨테이너와 트럭 수
    cont = list(map(int, input().split()))  # 컨테이너 종류
    peso = list(map(int,input().split()))   # 트럭 적재량
    #####
    '''
    1 5 3 
    8 3 
    은 
    5, 3  이 두개가 정답.
    '''
    ans = 0
    cont.sort(reverse=True)
    peso.sort()
    shipped = [0] * N
    while peso:
        w = peso.pop()
        for i in range(N):
            if w >= cont[i] and shipped[i] == 0:
                shipped[i] = 1
                ans += cont[i]
                break
    print(f'#{t} {ans}')
