def per(i,N):
    global numero

    if i == N: # 마지막
        # print(p)
        temp= 0
        for A in range(N):
            # 그냥 순열 억지로 시작 출발 사이에 만들어서 두칸을 하나씩 묶어서 계산합니다
            temp += ofc[p[A]][p[A+1]] # 임시값에 저장하고
        if temp < numero: # for 돌려서 계산한 결과
            numero = temp
        return # 네

    for j in range(N): # 맨 첫자리 제외.
        if used[j] == 0:
            p[i] = j
            used[j] = 1
            per(i+1,N)
            used[j] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    ofc = [list(map(int,input().split()))for _ in range(N)]
    # print(ofc)
    # 2차원 배열 속 각 c +1 의 idx가 N번 관리구역을 의미하는 듯 싶다.
    # 시작점과 끝점은 항상 1로 고정된다.
    # 따라서 관리구역은 N이 3인 경우 2 , 3 두개.
    # 4 의 경우 1,2,3 -> 1 부터 n-1 까의 순열을 구한다. / 각 구역은 1회씩 방문한다.
    used = [0]*N
    used[0] = 1
    p = [-1] * (N+1)
    p[0] = 0
    p[N] = 0
    numero = 123451235120
    per(1,N)
    print(f"#{t} {numero}")
