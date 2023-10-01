# piZza 굽-gi
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split()) # N 화덕 // M 피자
    pizza = list(map(int, input().split())) # 피 자 좋 아
    info = [] # 정 보 저 장 소
    idx = 1  # 몇 번 피 자 임 ?
    for c in range(0, N): # 냠
        k = pizza.pop(0)  # 냠 냠
        info.append([idx, k]) # 냠 냠 냠 냠
        idx += 1 # 냠 냠냠 냠냠냠 냠냠냠냠
    print(idx)
    print(info)
    while len(info) != 1:
        check = info.pop(0) # 나오시오! 그대는 우리 화덕을 떠나야 하오.
        if check[1] == 0: # 암튼 위에서 꺼낸거죠? 근데 너 치즈 다 녹았다?입니까?
            if pizza: # 피자피자피자? 새피자? 뉴피자? 신피자? 피자피자?  있다? 없다?
                info.append([idx, pizza.pop(0)]) # 새 피자를 피자피자피자
                idx += 1
        # else:
            check[1] = check[1]//2
            info.append(check)
    print(info)

    # print(info)