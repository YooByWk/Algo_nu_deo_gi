T = int(input())
for t in range(1,T+1):
    a = input()  # input() 자체가 str 임
    R = ''
    for i in a:
        R = i + R
    # print(a, R)
    if a == R:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')