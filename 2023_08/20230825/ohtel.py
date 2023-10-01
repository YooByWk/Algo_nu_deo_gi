def f(r, c, bw, N):
    board[r][c] = bw  # 어차피 놓을 수 있는 돌
    for dr, dc in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        nr, nc = r + dr, dc + c
        tmp = []
        while 0 <= nr < N and 0 <= nc < N and board[nr][nc] == op[bw]:  # 보드 내부, 반대 == 계속 이동
            tmp.append((nr, nc))
            nr, nc = nr + dr, nc + dc
        # 보드 내부이고 같은색이면
        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == bw: # 보드 내부, 같은색
            for p, q in tmp:
                board[p][q] = bw


B = 1;
W = 2
op = [0, 2, 1]

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())  # N 보드 크기 M 돌 놓 횟
    jugar = [list(map(int, input().split())) for _ in range(M)]
    board = [[0] * N for _ in range(N)]  # 0 -> N-1 인덱스
    # 중심에 4개의 돌 배치
    board[N // 2 - 1][N // 2 - 1] = W;
    board[N // 2 - 1][N // 2] = B;
    board[N // 2][N // 2 - 1] = B;
    board[N // 2][N // 2] = W
    for col, row, bw in jugar:  # 입력이 col, row colour
        f(row - 1, col - 1, bw, N) # 돌 놓기
    bcnt = wcnt = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == B:
                bcnt +=1
            elif board[r][c]:
                wcnt +=1
    print(f'#{t} {bcnt} {wcnt}')