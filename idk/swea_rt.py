"""
N 명 고객 방문 2 ~ 10
집 돌아감
회사 출발 > N 명 방문  중 최 단 거 리
이 문제는 가장 짧은 경로를 ‘효율적으로’ 찾는 것이 목적이 아니다.
여러분은 모든 가능한 경로를 살펴서 해를 찾아도 좋다.
모든 경우를 체계적으로 따질 수 있으면 정답을 맞출 수 있다.
"""
def per(i,N,minn,point):
    global mini

    if i = N:  # 다 내려갔을 때

    for j in range(N):
        if used[j] == 0:
            p[i] = (loc[4+(2*j)],loc[4+2*j+1])
            used[j] = 1
            per(i+1,N,minn+(
                abs(p[i][0]-point[0]),
            ))





T = int(input())
for t in range(1,T+1):
    N = int(input())
    loc = list(map(int, input().split()))
    # 0 0 100 100 70 40 30 10 10 5 90 70 50 20 // 2개씩..
    mini = 1231231231230
    used = [0]* N
    p = [0] * N
    st = [loc[0],loc[1]]
    home = [loc[2],loc[3]]
    per(0,N,mini,st)
