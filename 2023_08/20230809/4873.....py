#4866임
T = int(input())
for t in range(1, 1+T):
    res = 1
    check = input()
    st = []
    for c in check:
        if c in ['(', '{']:
            st.append(c)
        elif c in [')', '}']:
            if st:
                A = st.pop()
                if A == '(' and c == '}':
                    res = 0
                    break
                elif A == '{' and c == ')':
                    res = 0
                    break

            else : # if not st:
                res = 0
                break
    if st:
        res = 0
    print(res)

