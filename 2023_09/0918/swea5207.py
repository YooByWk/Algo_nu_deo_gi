# 이진 탐색
def binary(low, high, target, loc):
    global cnt

    if low > high:
        return

    mid = (low + high) // 2

    if A[mid] == target:
        cnt += 1
        return

    elif A[mid] < target and loc != 'right':
        return(binary(mid+1, high, target, 'right'))

    elif A[mid] > target and loc != 'left':
        return(binary(low, mid-1, target, 'left'))

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # print(A,B)
    A.sort()
    cnt = 0
    low = 0
    high = N-1
    loc = 'middle'

    for m in B:
        binary(low,high,m,'middle')

    print(f'#{t} {cnt}')
