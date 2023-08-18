T = int(input())
for t in range(1, T+1):
    N = int(input())
    limit = N // 2
    car = list(map(int, input().split()))
    ci = [0] * 31
    Sort = 0  # 결과
    # G = 0 # 큰작은중간 상자
    # M = 0 # 중간작은큰 상자
    # S = 0 # 작은큰중간 상자
    sh = [0,0,0]
    for c in car:
        ci[c] += 1
    # print(ci) # 이것은 하다 정리와 카운트. 절반 이상이 한 사이즈라면 그만.
    # print(ci.pop(max(ci)))
    # print(ci)
    for a in ci:
        if a > limit:
            Sort = -1
            print(f'#{t} {Sort}')
            break
    # 같은걸 넣어봅시다.
    cnt = 0
    new = []
    for c in ci:
        if c != 0:
            cnt +=1
            new.append(c)
    # print(new,'new')
    # new.sort()
    minn = 12313123
    num = len(new)
    for a in range(1,num):
        for b in range(a+1,num):
            G = new[:a]
            M = new[a:b]
            S = new[b:]
            A = max(sum(G), sum(M), sum(S))
            B = min(sum(G),sum(M),sum(S))
            D = A-B
            if min(sum(G),sum(M),sum(S)) == 0:
                # Sort = -1
                continue
            # elif max(sum(G),sum(M),sum(S))> N//2:
            #     miin = -1
            #     continue
            if D < minn:
                minn = D
    if Sort != -1:
        print(f'#{t} {minn}')
        # if Sort = -1:
        #     break


            # if len(new) > 0:
            #     v1 = new.pop()
            #     sh[i] += v1
            # else:
            #     break
            # if len(new) > 0:
            #     v2 = new.pop()
            #     sh[i] += v2
            # else:
            #     break
        # for i in range(3):
        #     if len(new) > 0:
        #         v2 = new.pop()
        #         sh[i] += v2
        #     else:
        #         break
            # if new:
            #     v2 = new.pop(min(new))
            #     sh[i] += v2
    # if 0 in sh:
    #     Sort = -1
    # elif Sort != -1:
    #     KKK = max(sh)-min(sh)
    #     print(f'#{t} {KKK}')


