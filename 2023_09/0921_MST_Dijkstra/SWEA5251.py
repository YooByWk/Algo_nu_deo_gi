#  5251. [파이썬 S/W 문제해결 구현] 7일차 - 최소 이동 거리 D3
#
# 마지막 주소 = N  도로 개수 E
# E 개 줄에 s e w
import heapq

def Dikstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0
    while pq:

        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for next in graph[now]:
            n_node = next[0]
            cost = next[1]

            n_cost = dist + cost

            if distance[n_node] < n_cost:
                continue

            distance[n_node] = n_cost
            heapq.heappush(pq,(n_cost,n_node))


T = int(input())
for tc in range(1, 1+T):
    N, E = map(int,input().split())
    graph = [[] for i in range(N+1)]
    for _ in range(E):
        f, t, w = map(int, input().split())
        graph[f].append([t, w])
    INF = 3456803754
    # print(graph)
    distance = [INF] * (N+1)
    Dikstra(0)

    print(f"#{tc} {distance[N]}")