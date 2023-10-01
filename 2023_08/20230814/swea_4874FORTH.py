def cal(v1,v2,op):
    if op == '+':
        return v1+v2
    if op == '*':
        return v1 * v2
    if op == '-':
        return v2 - v1
    if op == '/':
        return v2 // v1



def STEP2(s):
    st = []
    opp = 0 # 연산자
    nnn = 0 # 숫자
    for c in s:
        if c.isdigit():
            st.append(c)
            nnn += 1
        else:
            opp += 1
            if len(st) < 2:
                return 'error'
            v1 = st.pop()
            v2 = st.pop()
            st.append(cal(int(v1), int(v2), c))
    if len(st) == 1 :
        return st.pop()
    else:
        return 'error'
T = int(input())
for t in range(1,1+T):
    s = input().split()
    s.pop() # . 유기
    # print(s)
    res = STEP2(s)
    print(f'#{t} {res}')
