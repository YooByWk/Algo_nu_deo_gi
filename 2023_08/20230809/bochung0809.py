# import sys
# sys.stdin = open('input.txt')
#파스칼 삼각
T = int(input())
for t in range(1,T+1):
    # for 돌리고 list로 이전 값 저장
    #이전 값 개수 -1 만큼 for 돌림  더해야하는 값이 이전 값의 -1 이라서.
    N = int(input())
    before = [1] # 첫줄은 1
    print(f'#{t}')
    for _ in range(N):
        cur = []
        cur.append(1)
        for i in range(len(before) -1):
            num = before[i] + before[i+1] # 1 다음 수 계산
            cur.append(num) # 하나 쓱
        #중간 다 채우면 아래로 넘어감.
        cur.append(1) # 마지막 1 추가



        print(*before)
        before = cur