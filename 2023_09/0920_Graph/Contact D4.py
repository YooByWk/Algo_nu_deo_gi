# [S/W 문제해결 기본] 10일차 - Contact D4
from collections import deque
for t in range(1,11):
    N,S = map(int,input().split()) # S 에서 시작한다.
    member = list(map(int,input().split()))
    contact = [[] for _ in range(101)]
    # print(contact)
    for i in range(N//2):
        contact[member[2*i]].append(member[2*i+1])
    # print(contact)
    visited = [0] * (101)
    # print(visited)
    path = []
    max_depth = 0

    q = deque()
    q.append(S)
    visited[S] = 1
    while q:
        now = q.popleft()
        for next in contact[now]:
            if visited[next] == 0:
                q.append(next)
                visited[next] = visited[now]+ 1

    _max = 0
    for i in range(101):
       if visited[i] >= visited[_max]:
           _max = i

    # print(sorted(path,reverse=True))
    # print("아래가 답")
    # print(f"#{t} {max(path)}")
    print(f"#{t} {_max}")
