
def post(root):
    if cl[root]:
        post(cl[root])
    if cr[root]:
        post(cr[root])
    ca.append(arr[root])

def ans(lst):
    st = []
    while lst:
        aa = str(lst.pop(0))
        if aa.isdigit():
            st.append(int(aa))
        else:
            if aa == '+':
                v1 = st.pop()
                v2 = st.pop()
                res = v2 + v1
                st.append(res)
            elif aa == '-':
                v1 = st.pop()
                v2 = st.pop()
                res = v2 - v1
                st.append(res)

            elif aa == '*':
                v1 = st.pop()
                v2 = st.pop()
                res = v2 * v1
                st.append(res)

            elif aa == '/':
                v1 = st.pop()
                v2 = st.pop()
                res = v2 / v1
                st.append(res)
    return int(res)

T = 10
for t in range(1, T + 1):
    n = int(input())
    cr = [0] * (n+1)
    cl = [0] * (n+1)
    arr = [0] * (n+1)
    ca = []
    for k in range(n):
        tm = list(input().split())
        loc = int(tm[0])
        val = tm[1]
        if val.isdigit() == True:
            val = int(val)
        arr[loc] = val
        if len(tm) == 4:
            l=int(tm[2])
            r=int(tm[3])
            cr[loc]= r
            cl[loc]= l
    nah = post(1)
    print(f'#{t} {ans(ca)}')
