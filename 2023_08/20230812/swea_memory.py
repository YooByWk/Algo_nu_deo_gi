T = int(input())
for t in range(1,1+T):
    memory = list(input())
    # print(memory)
    st = []
    st.append(memory[0])

    if int(memory[0]) == 1: # 그냥 처음부터 확인하고 갈거임
        cnt = 1
        # print('nah')
    else:
        cnt = 0
    # cnt = 0
    # if st[0] == 1:  # 이상하게 작동을 안하길래
    #     cnt = 1
    #     print('nahh')
    for i in range(1, len(memory)):  # 메모리 받음
        c = st.pop()  #  뽑고
        if c != memory[i]:
            cnt += 1
        st.append(memory[i])  # 넣고
        # print(cnt)  # 처참한 실패의 흔적
        # if c != memory[i]:
        #     print(cnt,c,memory[i],'cnt, c, memo')
        # print(c,memory[i],'c','memo')
    print(f'#{t} {cnt}')
#  1로 시작하는 경우에 한개씩 부족한 경우가 있었음.
