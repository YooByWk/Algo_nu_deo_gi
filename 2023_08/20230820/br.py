T= int(input())
for t in range(1,1+T):
    N, M = map(int, input().split()) # N줄에 걸쳐 M 개씩 풍선에 든 종이 꽃가루가 나온다.
    pang = [list(map(int, input().split()))for _ in range(N)] # 리스트 입력받기
    # print(pang)
    cm = 0
    for r in range(N): # 3
        for c in range(M): # 5  예시상.
            temp = 0 # 임시 저장값입니다.
            powder = pang[r][c] # 해당 자리의 가루도 계산해야 합니다.
            temp += powder # 따라서 저장 후 그 자리에 넣어줍니다.
            for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:  # 델타
                for p in range(1,powder+1): # 델타에 곱해줄 영역입니다.  pang 의 숫자가 터진만큼 옆으로 더 터지니까
                    nr,nc = r + dr*p, c + (dc *p) # 델타 계산해서 새로운 자리
                    if 0<=nr<N and 0<=nc<M: # 범위 밖으로 나가지 않게
                        temp += pang[nr][nc] # 임시값에 더해주십니다.
                        if temp > cm: # 최대보다 크다면
                            cm = temp # 교체합니다.
    print(f'#{t} {cm}') # 정답 출력 예시는 #1 10 입니다.
