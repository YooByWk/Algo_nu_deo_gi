T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    # 배열은 N* N
    fly = [list(map(int, input().split())) for _ in range(N)]
    # print(fly[1][3])
    fmax = 0
    #파리채 만들기
    for rF in range(N-M+1): #탐색 위한 파리 리스트
        for cF in range(N-M+1): #탐색 위한 파리 리스트
            kill = 0
            for i in range(rF,rF+M): # 파리채의 크기
                for j in range(cF,cF+M): #파리채의 크기
                        kill += fly[i][j]
            if fmax < kill:
                fmax = kill
    print(fmax)

