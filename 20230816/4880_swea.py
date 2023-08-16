def game (lst):
    R = len(lst) // 2
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
    lft = lst[:R]
    print(lft,'lft')
    r8t = lst[R+1:]

    # lft = game(lst[:R])
    # print(lft, 'lft')
    # r8t = game(lst[R + 1:])

    return game((lft, r8t)) # 리스트루다가



for t in range(int(input())):
    N = int(input())
    info = []
    stu = list(map(int, input().split()))
    for j in range(N):
        info.append((j+1, stu[j]))
    print(info)
    print(game(info))
    # 1  2 가위 v 바위
    # 3  1 보 v 가위
    # 2  3 바위 v 보
