def search(r, c, k):
    global temp
    global cover

    if k == 1:
        if mapa[r][c] == 1 and cover[r][c] == 0:
            temp += 1
        cover[r][c] = 1
        return
    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N and cover[nr][nc] == 0:
            search(nr, nc, k - 1)
            if mapa[r][c] == 1 and cover[r][c] == 0:
                cover[r][c] = 1
                temp += 1



T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())  # 집들은 M만큼 돈을 준다
    mapa = [list(map(int, input().split())) for _ in range(N)]
    print(mapa)
    maximo = 0
    for r in range(N):# (N)

        for c in range(N): #(N)

            for k in range(N): #(N)
                cost = k * k + (k - 1) * (k - 1)  # K 는 N까지만 올려보자.
                temp = 0
                price = 0
                cover = [[0] * N for _ in range(N)]
                search(r, c, k)
                price = temp*M - cost
                if price > 0 and temp > maximo:
                    maximo = temp
    print(t,maximo)
