# 붕어빵 먹기 참 힘드네
# N 명이 먹음 \\ M초 지나면 K개 나옴
# 안기다리고 바로 쓱 먹을 수 있는가 봅시다
# for t in range(1, int(input())+1):
#     N, M, K = map(int, input().split()) # n 인원 / m 초에 k 개
#     tiempo = list(map(int, input().split()))
#     tiempo.sort()
#     seg = 0 # 초
#     persona = 0
#     pan = 0
#     while tiempo:
#         seg += 1
#         # persona += 1
#         if seg % M == 0:
#             pan += K
#         if seg == tiempo[0]:
#             tiempo.pop(0)
#             if pan > 0:
#                 pan -= 1
#                 # persona = 0
#             else:
#                 print(f'#{t} Impossible')
#                 break
#     else:
#         print(f'#{t} Possible') # 실패작
# for t in range(1, int(input())+1):
#     N, M, K = map(int, input().split())
#     tiempo = list(map(int, input().split()))
    # tiempo.append(0)
    # tiempo.sort()
    # s = 0
    # f = 1
    # while f <= len(tiempo)-1:
    #     if tiempo[f]-tiempo[f-1] < M and s <= 0:
    #         print(f'#{t} Impossible')
    #         break
    #     else:
    #         f += 1 # 첫바퀴 컷 나는거 구경
    #         s -= 1
    #     if  (f -1) % 2 == 0:
    #         s += M
    # else:
    #     print('pos')


for t in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    tiempo = list(map(int, input().split()))
    tiempo.sort()
    pan = 0
    # f = 0
    cnt = 1
    # int(k/m)
    res = 'Possible'
    # print(tiempo)
    if tiempo[0] < M:
        res = 'Impossible'
        # continue
    for cos in range(1,N):
        cnt += 1
        pan = tiempo[cos] // M * K
        if pan - cnt < 0:
            res = 'Impossible'
            break
    print(f'#{t} {res}')

