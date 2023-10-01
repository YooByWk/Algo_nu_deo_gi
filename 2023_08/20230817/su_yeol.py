for t in range(1, int(input())+1):
    N, M = map(int, input().split()) # M 번 뒤로 보내요
    Q = list(map(int, input().split()))
    print(f'#{t} {Q[M % N]}')

# 다시하기... Q 써서..