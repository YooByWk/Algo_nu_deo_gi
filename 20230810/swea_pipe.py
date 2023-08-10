T = int(input())
for t in range(1,1+T):
    check = input()
    # print(check[1])
    st = []
    k = len(check)
    tp = -1
    pi = 0
    cut = 0
    # while len(st)<k:

    for i in range(len(check)):
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
            else: #파이프 마감
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
# ((( () ( () () )) ( () )() )) ( () () )