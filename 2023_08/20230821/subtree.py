def subtree(root):
    passed.append(root)
    if cl[root]:
        subtree(cl[root])
    if N in passed:
        ans.append(root)
    if cr[root]:
        subtree(cr[root])





T = int(input())
for t in range(1, T+1):
    passed = []
    ans = []
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    # print(arr)
    cr = [0] * (E+2)
    cl = [0] * (E+2)
    p = [0] * (E+2)
    for i in range(0, len(arr), 2):
        pa = arr[i]
        c = arr[i+1]
        p[c] = pa
        if cl[pa] == 0:
            cl[pa] = c
        else:
            cr[pa] = c
    # print(cr)
    # print(cl)
    # print(p)
    root = N
    subtree(root)
    # print(passed)
    print(f'#{t} {len(ans)}')
