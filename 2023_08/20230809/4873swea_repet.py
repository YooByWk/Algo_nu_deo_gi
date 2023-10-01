T = int(input())
for t in range(1, T+1):
    letra = input() # 입력받기
    size = len(letra) # 문자열 길이
    st = [] # 리스트 미리 만들기
    st.append(letra[0]) # 어차피 한개는 꼭 들어가야 할 것 같음
    for d in range(1, size): # 1부터 마지막까지
        st.append(letra[d]) # 집어넣고
        if len(st) > 1: #비교가 가능한 상태라면
            if st[-2] == st[-1]: # 비교하고
                st.pop() # 같으면 둘다 ㅂㅂ
                st.pop()
    print(f'#{t} {len(st)}')


