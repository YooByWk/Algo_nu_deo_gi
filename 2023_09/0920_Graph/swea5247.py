#  5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산 D3
# 사용할 수 있는 연산 +1, -1, *2, -10
# N=2, M=7인 경우, (2+1) *2 +1 = 7이므로 최소 3 회
# case = [1, -1, *2, -10]
from collections import deque

def idk(number,cnt):
    global cnt_max

    q = deque()
    q.appendleft(number)
    visited[number] = 0
    while q:
        now = q.popleft()
        for next in [now+1, now-1, now*2, now-10]:
            if 0< next <= 1000000 and visited[next] ==0:
                q.append(next)
                visited[next] = visited[now] + 1
                if next == M:
                    # if cnt < cnt_max:
                    cnt_max = visited[now]
                    return





for t in range(1,int(input())+1):
    N, M = map(int, input().split())
    # N 에서 출발해서, 잘 뭔가 뭔가를 해서 뭔가 뭔가 하면 M 이 나온다.
    visited = [0] * 1000001
    cnt_max = 3458906534789
    idk(N,0)
    print(f'#{t} {cnt_max+1}')
