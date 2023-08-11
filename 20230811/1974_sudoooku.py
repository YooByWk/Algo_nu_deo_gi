def sudoku(arr): # 함수로 만들면 return을 통해 빠져나오기 좋다.
    for r in range(9): # 가 로
        check1 = []
        for c in range(9):
            check1.append(arr[r][c])
        if len(set(check1)) != 9:
            return 0
    for c in range(9): # 세로
        check2 = []
        for r in range(9):
            check2.append(arr[r][c])
        if len(set(check2)) != 9:
            return 0
    for r in range(0,9,3): # 3*3 확인
        for c in range(0, 9, 3):
            check3 = []
            for i in range(r, r+3):
                for j in range(c, c+3):
                    check3.append(arr[i][j])
            if len(set(check3)) != 9:
                return 0
    return 1



T = int(input())
for t in range(1,T+1):
    sdk = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{t}', sudoku(sdk))
