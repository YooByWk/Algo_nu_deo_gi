T = 10
for t in range(1,T+1):
    N = int(input())
    tokens = input()
    nums = '0123456789'
    stack = []
    fix = ''
    for token in tokens:
        if token in nums:
            fix += token
        else:
            if len(stack) == 0:
                stack.append(token)
            else:
                tmp = stack.pop()
                fix += tmp
                stack.append(token)

    fix += stack.pop()
    # print(fix)
    st = []
    res = 0
    for token in fix:
        if token in nums:
            st.append(token)
        else:
            v2 = st.pop()
            v1 = st.pop()
            res = int(v2) + int(v1)
            st.append(res)
        # print(st)
    print(f'#{t} {res}')