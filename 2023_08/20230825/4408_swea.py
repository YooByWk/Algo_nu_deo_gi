# 공간의 범위 만들기
# 홀수 짝수 나눠서
#
T = int(input())
for t in range(1,T+1):
    N = int(input()) # 학생 수
    arr = [list(map(int, input().split()))for _ in range(N)]

    cnt = [0] * 201  # 방 사이 공간을 지나는 사람의 수
    for a, b in arr: #  a<= b 라는 보장이 없다
        a = (a+a%2)//2
        b = (b + b%2)//2
        for i in range(min(a,b), max(a,b) +1):
            cnt[i] += 1  # 해당 공간을 지나는 사람의 수를 알게 된다
    print(f'#{t} {max(cnt)}')