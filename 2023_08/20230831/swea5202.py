# 도크의 사용 시간을 체크하자
T = int(input())
for t in range(1,T+1):
    N = int(input()) # 신청서
    table = []
    for i in range(N): # N 개의 신청서 입력받기
        table.append(list(map(int, input().split())))
    table.sort(key = lambda x :x[1])  # 람다 함수를 이용한 뒷자리 기준 정렬
    table = [[0,0]] + table # 하루의 시작
    # print(table)  # 디버그
    # [[0, 0], [4, 14], [8, 18], [17, 20], [20, 23], [23, 24]]
    #    0        1        2        3          4         5
    ans_lst = [] # 디버그
    ans = 0 # 정답용 숫자
    j = 0 # 이전 작업 인덱스 확인
    for i in range(1,N+1):
        if table[j][1] <= table[i][0]: # 이전 작업의 종료 시간이 다음 작업의 시작시간보다 작다면,
            ans_lst.append(i) # 디버그용 리스트
            ans += 1
            #j += i  # 마지막 작업은 해당 시간이 된다. # 더하지 말라고...
            j = i # 된다고 적어놓고 더하는 능지..수듄..
    # print(ans)
    print(f'#{t} {ans}')
