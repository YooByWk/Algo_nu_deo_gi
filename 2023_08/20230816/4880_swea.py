def game (lst):
    R = (len(lst)-1) // 2 + 1 # 범위설정 잘하자.
    if len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        if (lst[0][1] == 1 and lst[1][1] == 3) or\
            (lst[0][1] == 2 and lst[1][1] == 1) or \
                (lst[0][1] == 3 and lst[1][1] == 2) or \
                (lst[0][1] == lst[1][1]):
            return lst[0]
        else:
            return lst[1]

    lft = game(lst[:R]) # 리스트로 넣어야 작동해요
    # print(lft, 'lft')
    r8t = game(lst[R:]) # 그냥 잘라서 넣으면 애가 아파해서.. 재귀를 돌려야하니까 리스트로 넣자
    # print(r8t, 'r8t')
    return game([lft, r8t]) # 리스트루다가 # 튜플말고.


for t in range(1,int(input())+1):
    N = int(input())
    info = []
    stu = list(map(int, input().split()))
    for j in range(N):
        info.append((j+1, stu[j]))
    if len(info) % 2 == 1:
        info.append((info[-1]))
    # print(len(info))
    # print(info,'info')
    print(f'#{t} {game(info)[0]}')
    # 1  2 가위 v 바위
    # 3  1 보 v 가위
    # 2  3 바위 v 보
