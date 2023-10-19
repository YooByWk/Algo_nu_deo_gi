# swea 4866 괄호검사
'''
print('{} {}'.format(1, 2))
N, M = map(int, input().split())
print('#{} {}'.format(tc, find())
'''
T = int(input())
for t in range(1, 1+T):
    res = 1
    check = input()
    st = []
    for c in check:
        if c =='(' or c =='{':
        # if c in ['(','{']:     리스트가 더 깔끔하죠 + 인덱스까지!?
            st.append(c)
        if c ==')' or c =='}': # 필수같음
            if st:
                k = st.pop()
                # if ( c == '}' and k == '{') or (c ==')' and k == '('):
                #     pass
                if c == '}' and k == '(':
                    res = 0
                    break
                elif c == ')' and k == '{':
                    res = 0
                    break
                else:
                    res = 0
                    break
                    # if len(st) == 0:

                    #     # print('oui')
    if len(st) != 0:
        res = 0
    print(f'#{t} {res}')