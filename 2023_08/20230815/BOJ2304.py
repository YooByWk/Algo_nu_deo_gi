N = int(input()) # 1< N < 1000
Llst = []
Hlst = []
info = []
for t in range(N):
    L, H = map(int,input().split())
    Llst.append(L)
    Hlst.append(H)
    info.append((L, H))
longitud = max(Llst)-min(Llst) +1
Total = longitud * max(Hlst)
# print(info, '이차원으로 받긴 할거임')
# print(Total, '넓이')
# 왼쪽 오른쪽을 나눠서 접근해야해요
MaxL = Llst[Hlst.index(max(Hlst))]
MaxH = max(Hlst)
# print(MaxL, MaxH, '최고 높이의 위치와 최고높이')
info.sort() # 이제 위치가 오름차순으로 정렬됩니다. # 하지마.
# print(info)
# print(Hlst.index(max(Hlst))) # 넌 나가라
cur_L = info[0][0]
idx = -1
cur_H = info[0][1]
rcur_L = info[-1][0]
rcur_H = info[-1][1]
cnt = 0
# while cur_L != MaxL:
for i in range(len(info)-1):
    if info[i][1] < info[i+1][1]:
        # print(info[i][1],  info[i+1][1],'678678678678678')
        Total -= ((MaxH - cur_H) * ( info[i+1][0] - cur_L))
        cur_L = info[i+1][0]
        cur_H = info[i+1][1]
        # print(cur_L,cur_H,'l,h')
    if cur_L >= MaxL:
        # print('stfu')
        break
# 오른쪽에서 왼쪽으로
for i in range(len(info)-1, 1, -1):
    if info[i][1] < info[i-1][1]:
        # print(info[i][1],  info[i+1][1],'333333333333')
        Total -= (MaxH - rcur_H) * (rcur_L - info[i-1][0]  )
#         print(rcur_L,rcur_H,'l,h')

        rcur_L = info[i-1][0]
        rcur_H = info[i-1][1]
    if rcur_L <= MaxL:
#         print('callate')
        break
    # print('---------------------')
print(Total)