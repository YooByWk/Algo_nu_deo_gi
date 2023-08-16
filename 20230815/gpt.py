N = int(input())
info = []

# 기둥 정보 입력 받기
for _ in range(N):
    L, H = map(int, input().split())
    info.append((L, H))

# 왼쪽에서 오른쪽으로 가는 포인터
cur_L, cur_H = info[0]
Total = 0

for i in range(1, N):
    if info[i][0] <= cur_L:  # 이전 기둥의 오른쪽 위치보다 왼쪽에 있는 경우
        Total += (info[i][0] - cur_L) * cur_H
    else:  # 이전 기둥의 오른쪽 위치보다 오른쪽에 있는 경우
        Total += (info[i][0] - cur_L) * cur_H
        cur_L, cur_H = info[i]

# 오른쪽에서 왼쪽으로 가는 포인터
cur_L, cur_H = info[-1]

for i in range(N - 2, -1, -1):
    if info[i][0] >= cur_L:  # 이후 기둥의 왼쪽 위치보다 오른쪽에 있는 경우
        Total += (cur_L - info[i][0]) * cur_H
    else:  # 이후 기둥의 왼쪽 위치보다 왼쪽에 있는 경우
        Total += (cur_L - info[i][0]) * cur_H
        cur_L, cur_H = info[i]

# 가장 높은 기둥의 높이로 면적 추가
Total += cur_H

print(Total)
