s = '(6+5*(2-8)/2)'

def STEP1():
    result = []
    st = []
    icp = {'+': 1, '-' : 1, '*' : 2, '/' : 2, '(': 3}  # 코드로 있을 때
    # icp = in-coming priority
    isp = {'+': 1, '-' : 1, '*' : 2, '/' : 2, '(': 0}  # 스택에 있을 때
    # isp = in-stack priority
    for c in s:
        if c.isdigit():
            result.append(c)
        # elif c == '(':
        elif c == ')':
            while st and st[-1] != '(':
                v = st.pop()
                result.append(v)
            st.pop()  # 왼쪽 괄호 제거
        else:
            while st and isp[st[-1]] >= icp[c]: #if 보다는 while이 맞다.
                v = st.pop()
                result.append(v)
            st.append(c)
    while st:
        v = st.pop()
        result.append(v)
    return result
print(STEP1())
def cal(v1,v2,op):
    if op == '+':
        return v1 + v2
    if op == '-':
        return v2 - v1
    if op == '*':
        return v1 * v2
    if op == '/':
        return v2 // v1

def STEP2(s):
    st = []
    for c in s:
        if c.isdigit():
            st.append(c)
        else:
            v1 = st.pop()
            v2 = st.pop()
            st.append(cal(int(v1), int(v2), c))
    return st.pop()
step1_s = STEP1()
res = STEP2(step1_s)
print(res)

