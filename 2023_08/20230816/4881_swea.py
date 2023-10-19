# def f(i, N):
#     if i == N:
#         print(A)
#     else:
#         for j in range(i, N): # 자신부터 오른쪽 끝까지
#             A[i], A[j] = A[j], A[i]
#             f(i+1, N)
#             A[i], A[j] = A[j], A[i] # 이거 없으면 안됨 # 원상복구

# 다시 해보기
def f(k, curM):
    global res
    if curM > res:
        return
    if k == N:
        # for kt in range(N):
        #     c = result[kt]  # 백트레킹...할라구...
        #     sumV += arr[kt][c]
        if curM < res:
            res = curM
        return

    for i in range(N):
        if not used[i]:
            used[i] = True
            result[k] = i
            f(k + 1,curM+arr[k][i]) # 중간합으로 내려올 수 있게
            used[i] = False
    return


T = int(input())
for t in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = [-1] * N
    used = [False] * N
    res = 10 * 10 * 10
    f(0,0)
    print(f'#{t} {res}')

A = [0, 1, 2]