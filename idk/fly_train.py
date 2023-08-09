T = int(input())
for t in range(1, 1+T):
    D, A, B, F = map(int, input().split())
    print(f'#{t}',((D / (A+B)) * F))
