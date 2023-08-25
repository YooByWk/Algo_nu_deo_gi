# print(int(0x5F))
# 만들 수 있는 k번째 수
# N 개의 숫자 - 4의 배수 8 이상 28 이하
# 회전 수 ? 일단 각 4개 임
T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    num = list(input())
    rot = N // 4  # 12 // 4 == 3 (3바퀴)
    test = []
    for tn in range(rot): # rot 번 뒤로 돌림
        for i in range(0,N,rot): #
            temp = ''
            for j in range(i,i+rot):
                temp += num[j]
            test.append(temp)
        p = num.pop(0) # 안에서 한바퀴 잘 정리해서 넣으면
        num.append(p) #뽑았다가 맨뒤로 넣기
    ffff = list(set(test))
    nah = []
    for i in ffff:
        asdf = int(i,16)
        nah.append(asdf)
    nah.sort()
    # print(nah)
    print(f'#{t} {nah[-K]}')
