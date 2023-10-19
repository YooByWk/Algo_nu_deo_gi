T   = 10
for t in range(1, 1+T):
    N=int(input())
    char = input()
    nums = '0123456789'
    stack = []
    fix = ''
    for c in char:
        if c in nums:
            fix += c
        else: #  연산자의 자리
            if c == '*':
                while  len(stack) != 0 and stack[-1] != '+':
                    fix += stack.pop() # +가 아닐떄까지 뽑아서 넣는다 // +의 우선순위는 *보다 낮다
                stack.append(c) # 그러고 나서 방금 뽑은 연산자 넣어주기
            elif c == '+': # +는 딱히 뭔 권력이 없어요.
                while len(stack) != 0:
                    fix += stack.pop() # + 기호 첨가.
                stack.append(c) # 일 다했으면 또 하나 넣어줘야죠
    while len(stack):
        fix += stack.pop()
    # print(fix)
    # 변환 완료.
    # 계산하기
    st = []
    res = 0
    for c in fix:
        if c in nums:
            st.append(c)
        else:
            if c == '+':
                v2  = st.pop()
                v1 = st.pop()
                res = int(v2) + int(v1)
                st.append(res)
            elif c == '*':
                v2 = st.pop()
                v1 = st.pop()
                res = int(v2) * int(v1)
                st.append(res)

    print(f'#{t} {res}')