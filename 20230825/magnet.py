N = 1; S = 2  # 1은 아래로, 2는 위로


for tc in range(1, 11):
    table = int(input())
    lst = [list(map(int, input().split())) for _ in range(table)]
    cnt = 0
    for c in range(table):
        stuck = 0
        for r in range(table):
            if lst[r][c] == 2 and stuck ==1:
                stuck = 0
                cnt += 1
            elif lst[r][c] == 1:
                stuck =1

    print(cnt)