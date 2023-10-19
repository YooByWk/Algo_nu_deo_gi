T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    resto = [list(map(int, input().split())) for _ in range(N)]  # 리스트 만들기
    # print(resto)
    maximo = 0  # 최대 저장
    for r in range(N):
        temp = 0  # 줄바뀜 = 초기화
        for c in range(M):
            if resto[r][c] == 1:
                temp += 1 # 무지성 덧셈
                # print(temp,'t')
            else:  #다르면 초기화
                if temp > maximo:
                    maximo = temp  # 초기화 전에, 최대보다 크다면 저장
                temp = 0   # 초기화

        if temp > maximo:
            maximo = temp

    for c in range(M):  # 순서를 바꿔서
        temp = 0  # 임시 저장
        for r in range(N):
            if resto[r][c] == 1:
                temp += 1  # 맞으면 +1
                # print(resto[r][c])
                # print(temp,'t')
            else:
                if temp > maximo:
                    maximo = temp  # 초기화 이전 더 크다면 저장
                temp = 0

        if temp > maximo:
            maximo = temp   # 부등호 방향 조심하기

    print(f'#{t} {maximo}')