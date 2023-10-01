def dfs(r,c):
    visited = [[False] * N for _ in range(N)]
    st = []
    st.append((r,c))
    visited[r][c] = True
    while st:
        vr, vc = st.pop()
        if lst[vr][vc] == 3:
            # print(lst[vr][vc])
            return 1
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]: #delta
            newR = vr + dr
            newC = vc + dc
            if 0 <= newR < N and 0 <= newC < N:
                if lst[newR][newC] ==0 or lst[newR][newC] == 3 :
                    if not visited[newR][newC]:
                        st.append((newR,newC))
                        visited[newR][newC] = True
    else:
        return 0
# 0은 통로, 1은 벽, 2는 출발, 3은 도착

T = int(input())
for t in range(1, 1+T):
    Ri = 0
    Cj = 0
    N = int(input())
    lst = [list(map(int, (input())))for _ in range(N)]
    # print(lst)
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 2:
                Ri = i
                Cj = j  # 시작점 찾기 인가
    # print(Ri,Cj)
    res = dfs(Ri,Cj)
    print(f'#{t} {res}')
