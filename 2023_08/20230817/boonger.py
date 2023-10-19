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
    N, M, K = map(int, input().split()) # N 손님, M 초 , K개
    tiempo = list(map(int, input().split()))
    tiempo.sort() #도착 순서 정렬
    pan = 0
    # f = 0
    cnt = 1 # 사람의 수 , 0초의 경우
    res = 'Possible'
    print(tiempo)
    if tiempo[0] < M: # 0 초의 경우는 여기서 해결되는거라 아래 for는 1에서 출발
        res = 'Impossible' # 0초에 손님이 왔는데 붕어빵이 없다면, 불가능
    for cos in range(1,N): # N은 사람이다. 따라서 N 1개당 1명임.
        cnt += 1 # 그래서 N 개수 따라서 사람  더해줌 # 도착순서 정렬은 필요함
        pan = tiempo[cos] // M * K #
        if pan - cnt < 0:
            res = 'Impossible'
            break
    print(f'#{t} {res}')

