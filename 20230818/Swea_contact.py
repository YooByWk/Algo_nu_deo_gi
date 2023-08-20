"""
24 2
100 17 39 22 100 8 100 7 7 100 2 7 2 15 15 4 6 2 11 6 4 10 4 2
"""


def emer(start):
    global P_max  # 혹시 모르니까 일단
    q = []  # 가능한지 보는거면 dfs도 가능할것같은데 // 아니요 안됨.
    visited = [0] * 101  # 방문여부
    q.append(start)  # 일단은 시작점 집어넣기.
    visited[start] = 1
    # print(q, 'Q')
    # ------------준비완료----------
    while q:  # q에 원소가 있는 한
        t = q.pop(0)  # dfs 안될것같음
        # if P_max < t: # 지금 방문 중인 인간 번호 확인 中
        #     P_max = t # 방문한 인간의 번호 가장 큰 것 기억하기. // 필요없음. 마지막 경우만 알면 됨
        for llamado in connect[t]:  # t 라는 인간의 연락망에서 연락을 돌려요
            if visited[llamado] == 0:  # llamado는 스페인어로 called 정도의 의미를 지닙니다.
                q.append(llamado)
                visited[llamado] = visited[t] + 1
                if P_max < visited[llamado]:
                    P_max = visited[llamado]
                # print(t, connect[t])
                # print(visited[llamado],'거리')  # 실험실
                # print(P_max)
    for k in range(len(visited)):  # 인덱스로 안하고 하니까 P_max에 고정되더라구요
        if visited[k] == P_max:
            res.append(k)  # 가장 멀리 ( 늦게 ) 연락 받은 사람들은 P_max가 동일할 것.
    return max(res)  # 그 중 가장 높은 번호를 return


T = 10
for t in range(1, 1 + T):
    P_max = 0  # 방문 여부 확인용
    res = []  # 임시로 저장
    M, S = map(int, input().split())
    memb = list(map(int, input().split()))
    connect = [[] for _ in range(101)]  # 100명까지
    for i in range(M // 2):  # 연결된 리스트를 만들어보자.  \\ 단방향이다
        v1 = memb[i * 2 + 1]  # 일단 뭐
        v2 = memb[i * 2]  # 이렇게 받아서
        connect[v2].append(v1)  # 이쁘게 집어넣으면 완
    # emer(S) 실험용 함수 호출
    print(f'#{t} {emer(S)}')
