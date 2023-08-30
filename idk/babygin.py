T = int(input())
for t in range(1,T+1):
    carta  = list(map(int,input().split()))
    p1_cnt = [0]*10 # 1p 카드 리스트
    p2_cnt = [0]*10  # 2p 카드 리스트
    terminar = 0

    for i in range(0,12,2): # 각 6장
        if terminar ==1:
            break

        p1_cnt[carta[i]] += 1
        if p1_cnt[carta[i]] == 3:
            print(f'#{t} 1')
            terminar = 1
            break
        #  여기까지 tri 확인

        for j in range(8):
            if p1_cnt[j] != 0 and p1_cnt[j+1] != 0 and p1_cnt[j+2] != 0:
                print(f'#{t} 1')
                terminar = 1
                break
        if terminar ==1:
            break



        p2_cnt[carta[i+1]] += 1
        if p2_cnt[carta[i+1]] == 3:
            print(f'#{t} 2')
            terminar = 1
            break

        for j in range(8):
            if p2_cnt[j] != 0 and p2_cnt[j+1] != 0 and p2_cnt[j+2] != 0:
                print(f'#{t} 2')
                terminar = 1
                break
        if terminar ==1:
            break

    if terminar != 1:
        print(f'#{t} 0')