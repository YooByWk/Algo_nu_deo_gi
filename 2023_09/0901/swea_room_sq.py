def move(r,c, vez):
    global cnt
    global t_lst
    dr = [0, 0, 1, -1]
    dc = [-1, 1, 0, 0]
    cur = room[r][c]
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            if room[nr][nc] -1 == cur:
                move(nr, nc, vez +1 )
    if vez >= cnt:
        cnt = vez
        t_lst.append([cnt,cur-cnt+1])


T= int(input())
for t in range(1,T+1):
    N = int(input())
    room = [list(map(int, input().split()))for _ in range(N)]
    cnt = 1
    t_lst = []
    for r in range(N):
        for c in range(N):
            k = move(r,c,1)
    t_lst.sort(reverse=True)
    ans =[]
    for s in t_lst:
        maxx = t_lst[0][0]
        if s[0] == maxx:
            ans.append(s)
        else:
            break
    ans.sort()
    print(f'#{t} {ans[0][1]} {ans[0][0]}')
