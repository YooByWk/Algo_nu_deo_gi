T = int(input())
for t in range(1,T+1):
    n,m = map(int,input().split())  # 인풋을 잘 확인하자... 제발 까먹지 말자..
    Aj = list(map(int, input().split()))  # 리스트 받기 (인덱스용)
    Bj = list(map(int, input().split()))  # 리스트 받기 (인덱스용)
    la = len(Aj)  # N 있지만 해봤어요 # 더 직관적인것 같
    lb = len(Bj)  # M 있지만 해봤어요 # 음
    cm = -9999
    if lb > la:
        for i in range(lb - la+1):  # 길다란놈 - 짧은놈 +1 (idx) 이러면 아무튼 필요한 만큼을 함. 아래에 N칸 튀어나가는 애들 때문에
            temp = 0  # 초기화 위치 여기 맞음
            for j in range(la):  # 짧은놈을 반복해야하니까
                # print(temp)
                temp += Aj[j] * Bj[i + j]
                # print('temp',temp,'aj',Aj[i],'bj', Bj[i+j], cm,i)
            if cm < temp:
                cm = temp  # 비교 교체
    else:
        for i in range(la - lb+1):  # 아무튼 위랑 같음
            temp = 0  # 초기화 여기 맞음
            for j in range(lb):
                temp += Bj[j] * Aj[i+j]
            if cm < temp:
                cm = temp  # 비교, 교체
    print(f'#{t} {cm}')
