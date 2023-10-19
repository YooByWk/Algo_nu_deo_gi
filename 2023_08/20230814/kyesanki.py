# def step1():
#     pass
#
# T = 10
# for t in range(1,1+T):
#     n = int(input())
#     s = input()
#     st = []
#     # print(s)
#     for i in s:
#         if i.isdigit():
#             st.append(i)
#         else:

def STEP1():
    result = []
    st = []
    icp = {'+': 1, '-' : 1, '*' : 2, '/' : 2, '(': 3}  # 코드로 있을 때
    # icp = in-coming priority
    isp = {'+': 1, '-' : 1, '*' : 2, '/' : 2, '(': 0}  # 스택에 있을 때
    # isp = in-stack priority
    for c in s:
        # print(st)
        if c.isdigit():
            result.append(c)
        else:
            while st and isp[st[-1]] >= icp[c]: #if 보다는 while이 맞다.
                v = st.pop()
                result.append(v)
            st.append(c)

    # while st:
    #     v = st.pop()
    #     result.append(v)
    return result

def STEP2(s):
    st = []
    for c in s:
        if c.isdigit():
            st.append(c)
        else:
            v1 = st.pop()
            v2 = st.pop()
            st.append(cal(int(v1), int(v2), c))
            print(st)
    return st.pop()


def cal(v1,v2,op):
    return v1 + v2

T = 10
for t in range(1,1+T):
    n = int(input())
    s = input()
    # print(STEP1())
    sss = STEP1()
    res = STEP2(sss)
    print(res)

