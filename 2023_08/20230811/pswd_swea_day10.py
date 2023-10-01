for t in range(1,11):
    n, my_str = input().split()
    # print(n,str)
    N = int(n)
    # print(nn)
    stack = [0] * N
    top = -1
    ans = ''
    for i in my_str:
        if top == -1 or stack[top] != i:
            top += 1
            stack[top] = i
        else:
            top -= 1
    for j in range(top+1):
        ans += stack[j]
    print(f'#{t} {ans}')