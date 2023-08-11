for t in range(1, 11):
    N = int(input())
    case = input()
    L_lst = ['(', '[', '{', '<']
    R_lst = [')', ']', '}', '>']
    st = []
    tp = -1
    res = 1

    for i in case:
        if i in L_lst:
            st.append(i)
        if i in R_lst:
            if st:
                p = st.pop()
                if L_lst.index(p) != R_lst.index(i):
                    res = 0
                    break
    else:
        if len(st) != 0:
            res = 0
    print(f'#{t} {res}')
