def 檢(初,末):
    vst = [[False] * 16 for _ in range(16)]
    # 路[1][1]
    輯 = [] # 집
    輯.append((初,末))
    vst[1][1] = True
    while 輯:
        임시行,임시列 = 輯.pop(0)
        if 路[임시行][임시列] == 도착점:
            return 1
        for 行,列 in [[0,1],[1,0],[-1,0],[0,-1]]:
            新行 = 임시行 + 行
            新列 = 임시列 + 列
            if 0 <= 新行 < 16 and 0<= 新列 < 16 and 路[新行][新列] != 1 and vst[新行][新列] == 0:
                輯.append((新行,新列))
                vst[新行][新列] = True

    return 0

def ㅁㄴㅇㄹ():
    for ㅎ in range( 16):
        for ㅇ in range (16):
            if 路[ㅎ][ㅇ] == 2:
                return ㅎ,ㅇ

試驗 = 10
for 出 in range(1,試驗+1):
    數 = int(input())
    路 = [list(map(int, input())) for _ in range(16)]
    ㅁㄴㅇㄹ()
    도착점 = 3
    print(f'#{出} {檢(1, 3)}')
