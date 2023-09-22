T = int(input())
import heapq

INF = 1e9


def Dijkstra(start,gp,ds):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if ds[now] < dist:
            continue

        for next in gp[now]:
            next_node = next[0]
            cost = next[1]

            new_cost = dist + cost

            if ds[next_node] <= new_cost:
                continue

            ds[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))

    return ds



for tc in range(1, T + 1):
    N, M, X = map(int, input().split())
    # M 개의 출
    graph = [[] for i in range(N + 1)]
    distance = [INF] * (N + 1)
    anti_graph = [[] for i in range(N+1)]
    anti_distance = [INF] * (N+1)
    for _ in range(M):
        f, t, w = map(int, input().split())
        graph[f].append([t, w])
        anti_graph[t].append([f,w])

    Dijkstra(X,graph,distance)
    Dijkstra(X,anti_graph,anti_distance)
    # print(distance[1:])
    # print(anti_distance[1:])
    _max  = 0
    for i in range(1,N+1):
        t_max = distance[i] + anti_distance[i]
        if t_max > _max:
            _max = t_max
    print(f"#{tc} {_max}")