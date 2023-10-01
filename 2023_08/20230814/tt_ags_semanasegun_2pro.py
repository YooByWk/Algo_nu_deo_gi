def check(s):
    pass


def cal(s):
    st = []
    for c in s:
        if c == ")":
            tmp = 0
            while st and st[-1] != '(':
                tmp += int(st.pop())
            if st:
                st.pop()
                st.append(tmp)
            else:
                return -1
        elif c == "}":
            tmp = 1
            while st and st[-1] != '{':
                tmp *= int(st.pop())
            if st:
                st.pop()
                st.append(tmp)
            else:
                return -1
        else:
            st.append(c)
    if len(st) == 1:
        return st.pop()
    else:
        return -1
