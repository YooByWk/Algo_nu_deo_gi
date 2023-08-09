T = int(input())
for t in range(1,T+1):
    N, Q = map(int, input().split())
    box = [0] * N
    for i in range(Q):
       num = i + 1
       stt, fin = map(int, input().split())
       for j in range(stt-1, fin):
           box[j] = num
    print(f'#{t}', *box)