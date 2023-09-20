# #프로세서

# def valid(r,c,dr,dc):
#     k = 1
#     while 0<=r+dr*k<N and 0<=c+dc*k<N:
#         if arr[r+dr*k][c+dc*k]==1:
#             return False
#         k+= 1
#     return True
#
# # r,c 에서 dr, dc 방향으로 값을 채운다.
# def setting(r,c,dr,dc,value):
#     k =1
#     while 0<=r+dr*k<N and 0<=c+dc*k<N:
#         if arr[r + dr * k][c + dc * k] == value:
#             k+1
#         return k


def dfs(n):
    # 코어의 자리에서 시작해야 한다.
    r = core[n][0]
    c = core[n][1]
    visited[n] = 1
    # 우선 다음 코어를 호출해야 한다

    # 호출이 끝났으니 방향을 정한다.
    for d in range(4):
        dr = d_row[d]
        dc = d_col[d]

        # 방향을 정했으니 연결한다.

        # 연결이 됐다면

        # 연결이 안됐다면

        # 코어의 연결 개수를 확인

        # 가장 높다면 전선의 개수를 확인




T = int(input())
d_row = [1, -1, 0, 0]
d_col = [0, 0, 1, -1]
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    core = []
    max_core = 0
    min_wire = 456789123456
    for r in range(1,N-1):
        for c in range(1,N-1):
            if arr[r][c] == 1:
                core.append((r,c))
    visited = [0]*len(core)
