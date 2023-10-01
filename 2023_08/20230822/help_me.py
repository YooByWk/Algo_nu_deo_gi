# def change(lst):
#     code = {
#         '0': '0000', '1': '0001', '2': '0010', '3': '0011',
#         '4': '0100', '5': '0101', '6': '0110', '7': '0111',
#         '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
#         'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
#     }
#     return code[lst]
#
# import sys
# sys.stdin = open('input.txt', 'r')
def htob(hell):  # 16 -> 10
    code = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    return code[hell]
# print(htob('F'))


cipher = [1123,1222,2212,1141,2311,1321,4111,2131,3121,3112,1123]


T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())

    ori = [input() for _ in range(N)]
    bina = ['' for _ in range(N)]
    test = ['' for _ in range(N)]
    for r in range(N):
        for c in range(M):
            bina[r] += htob(ori[r][c])
        test[r] = bina[r][::-1]
        test[r] = int(test[r])
        test[r] = str(test[r])
        # test[r] = test[r][::-1] # 지독한 슬라이싱의 흔적
    # print(test) # 암호만 남김
    clave = 0
    for r in range(N):
        tc = len(test[r])-1
        c = 0
        if tc < 56:
            continue
        while c <= tc:
            # 암호 코드는 8개
            for i in range(8):
                # 암호는 항상 4개의 숫자로 나온다.
                # 그리고 시작은 항상 1로 한다. (역수 기준)
                c1,c2,c3 = 0,0,0
                temp = ''
                while test[r][c] == '1'and c<tc:
                    c += 1
                    c1 +=1
                while test[r][c] == '0' and c<tc:
                    c += 1
                    c2 += 1
                while test[r][c] == '1'and c<tc:
                    c += 1
                    c3 += 1
                while test[r][c] == '0' and c<tc:
                    c +=1
                c1,c2,c3 = int(c1),int(c2),int(c3)
                vez = min(c1,c2,c3)
                if vez != 0:
                    v1,v2,v3 = c1//vez, c2//vez, c3//vez
                    temp += str(v1) + str(v2) + str(v3)
                    print(temp)
                else:
                    continue
    # print(temp)

# h = '4F'
# k = int(h,16)
# s = []
#
# for j in range(8):
#     t = k & (1<<j)
#     if t != 0:
#         s.append('1')
#     else:
#         s.append('0')
# print(s)
# print(bin(k))

