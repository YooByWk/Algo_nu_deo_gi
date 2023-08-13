T = int(input())
for t in range(1,1+T):
    ori = input()
    res = 0
    for i in range(1,11):
        pt = ori[:i]
        npt = ori[i:2*i]
        if i != 0 and pt == npt:
            res = len(pt)
            break
    print(f'#{t} {res}')
