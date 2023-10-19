def in_order(root):  # 중위 탐색
    global num
    if root > N:
        return
    in_order(root * 2)
    arr[root] = num
    num += 1
    in_order(root * 2 + 1)




T = int(input())
for t in range(1, T+1):
    N = int(input())
    num = 1
    arr =[0] * (N+1)
    in_order(1)
    print(f"#{t} {arr[1]} {arr[N // 2]}")
