for _ in range(1, 11):
    t, r = map(int, input().split())
    # print(t, r,  't , r ')
    # 0 1/ 0 2 / 1 4 / 1 3/  4 8 | 4 3| 2 9| 2 5| 5 6 | 5 7/ 7 99/ 7 9 /9 8/ 9 10/ 6 10/ 3 7/ #2개씩 자르렴
    temp = list(map(int, input().split()))
    # print(temp)
    # print(len(temp))
    start = 0
    end = 99
    st = []
    visit = [False] * 100
    G = [[] for a_ in range(100)]
    for idx in range(0,len(temp),2):
        L = temp[idx]
        R = temp[idx+1]
        G[L].append(R)
    # print(G)
    st.append(0)
    while st: # 스택이 있을 때
        v = st.pop()
        if not visit[v]:
            visit[v] = True
            if v == 99:
                print(f'#{t} 1')
                break
        for w in G[v]:
            if not visit[w]:
                st.append(w)
    else:
        print(f'#{t} 0')
