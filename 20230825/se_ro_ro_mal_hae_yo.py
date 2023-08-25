T = int(input())
for t in range(1, T + 1):
    lst = [list(input()) for _ in range(5)]
    # print(lst)
    rango = 0
    minn = 1111
    ans = ''
    for j in lst:
        temp = len(j)
        if temp > rango:
            rango = temp
        if temp < rango:
            rango = temp
        for c in range(rango):
        # while lst:
            for r in range(5):
                # print(lst[r])
                if lst[r]:
                    ans += lst[r].pop(0)
                elif not lst[r]:
                    continue
    print(f"#{t} {ans}")
