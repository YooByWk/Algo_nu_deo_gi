T = int(input())
for t in range(1,1+T):
    check = input()
    # print(check[1])
    st = [] # 스 택인가?
    k = len(check)  # 괄호지옥
    tp = -1 # 나름 스택이니까 top 있어야지...
    pi = 0 # 잘릴 파이프의 수
    cut = 0 # 누적 절단
    # while len(st)<k:

    for i in range(len(check)): # 파이프 길이만큼 하려구요
        if check[i] == '(':
            st.append(check[i]) # 아 몰라 일단 append 해
            pi += 1 # 파이프 수량 +1
            tp += 1 # 스택 탑 +1
        else: # )의 경우
            if check[i-1] == '(': #한칸 이전이 열리는거라면, 레이저
                st.pop()
                pi -= 1
                cut += pi
                tp -= 1
            else: #파이프 마감 #한개만 늘어난다.
                st.pop()
                pi -= 1
                cut += 1
                tp -= 1
        if tp <-1:
            print('죽었어요', cut )
            break
    # print(cut, tp, 'ct and tp')
    # print(pi)
    print(f'#{t} {cut}')
# ((( () ( () () )) ( () )() )) ( () () ) #인풋 잘라서 확인하는 용도