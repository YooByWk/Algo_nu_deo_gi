# import sys
# sys.stdin = open('input.txt', 'r')
def HexToBin(hell): # 16 -> 10
    code = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    return code[hell]


PAT = [211, 221, 122, 411, 132,
       231, 114, 312, 213, 112]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    hexArr = [input() for _ in range(N)]
    binArr = ['' for _ in range(N)]

    for r in range(N):
        for c in range(M):
            binArr[r] += HexToBin(hexArr[r][c])
    ans = 0
    for row in range(1, N):
        if '1' not in binArr[row]:
            continue

        col = len(binArr[0]) - 1
        while col >= 56: # 애초에 그 줄의 길이는 56보다 길다.
            if binArr[row][col] == '1' and binArr[row - 1][col] == '0':  # 2진법 리스트에 있는 1 중 아랫줄 0인곳
                result = [] # 결과
                for i in range(8):  # 코드가 8개라서
                    cnt1 = 0
                    while binArr[row][col] == '1': # 여기는 코드 내부의 숫자들을 확인하는 while 친구들
                        cnt1 += 1
                        col -= 1
                    cnt2 = 0
                    while binArr[row][col] == '0':
                        cnt2 += 1
                        col -= 1

                    cnt3 = 0
                    while binArr[row][col] == '1':
                        cnt3 += 1
                        col -= 1

                    while binArr[row][col] == '0':
                        col -= 1

                    ratio = min(cnt3, cnt2, cnt1) # 배율을 알아내기 위함, 항상 1개짜리 경우의 수가 있었음
                    t = cnt3 // ratio * 100 + cnt2 // ratio * 10 + cnt1 // ratio
                    result.insert(0, PAT.index(t))
                res_sum = 0
                for i in range(4):
                    res_sum += result[i * 2] * 3 + result[i * 2 + 1]
                # print(res_sum)
                if res_sum % 10 == 0:
                    # sum(result)
                    ans += sum(result)
            else:
                col -= 1

    print(f'#{tc} {ans}')