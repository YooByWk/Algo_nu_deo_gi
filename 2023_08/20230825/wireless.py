# a,b 위치로 시점의 최대 충전량?
def chg(posA, posB):
    cha = []
    chb = []
    for i in range(A):
        x,y, c,p =bat[i]
        if abs(posA[0] - x) + abs(posA[1] - y) <= c:
            cha.append((i, p))
        if abs(posB[0] - x ) + abs(posB[1]-y) <= c:
            chb.append((i, p))
    # print(cha,chb)
    if cha and not chb:
        return cha[0][1]
    if chb and not cha:
        return chb[0][1]
    if cha and chb:
        if cha[0] != chb[0]:
            return cha[0][1] + chb[0][1]
        nextA = nextB = 0
        p = cha[0][1]
        if len(cha) >= 2:
            nextA = cha[1][1]
        if len(chb) >= 2:
            nextB = chb[1][1]
    else:
        return 0

    return max(p, p+nextA, p+nextB)


    # return 0


T = int(input())
for tc in range(1, T + 1):
    M, A = map(int, input().split())
    moveA = list(map(int, input().split())) # A의 이동경로  0;1; 2; 3; 4; 이동 방향; 이동하지 않음; 상 (UP); 우 (RIGHT); 하 (DOWN); 좌 (LEFT)
    moveB = list(map(int, input().split())) # B의 이동경로
    bat = [list(map(int, (input().split()))) for _ in range(A)]
    bat.sort(reverse=True,key=lambda x : x[3]) # 각 리스트 중 가장 큰 것에 저장했다.)
    dx = [0, 0, 1, 0, -1] # ㄱ ㅖ ㅅ ㅏ ㄴ
    dy = [0, -1, 0, 1, 0] # ㄱ ㅖㅅ ㅏ ㄴ

    posA = [1, 1]
    posB = [10, 10]
    res = 0
    res += chg(posA, posB)
    for i in range(M):
        posA[0] += dx[moveA[i]]
        posA[1] += dy[moveA[i]]
        posB[0] += dx[moveB[i]]
        posB[1] += dy[moveB[i]]
        res += chg(posA,posB)
    print(f'#{tc} {res}')
