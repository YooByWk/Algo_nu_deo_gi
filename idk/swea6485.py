#swea 6485
T = int(input())
for t in range(1, T+1):
    N = int(input())
    cnt = [0] * 5001 # 1~5000 을 지나는 노선 수
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1): # a에서 b 까지 지나거라.
            cnt[i] += 1 #노선이 그 구간을 지나감을 의미함
        P = int(input())
        bus_stop = [int(input()) for _ in range()]
        print(f'#{t}}', end = ' ')
