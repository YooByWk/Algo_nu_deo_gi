def ans(r,c,minn):
    global kkk # 함수 외부...
    if r == (N-1) and c == (N-1):
        minn += nums[r][c]
        if minn < kkk:
            kkk = minn
        return
    if  r < N-1 and minn < kkk:
        ans(r+1,c,minn+nums[r][c])
    if c < N-1 and minn < kkk:
        ans(r,c+1,minn+ nums[r][c])


T = int(input()) # 인풋 받음
for t in range(1,T+1): # 테케
    N = int(input()) # N*N
    nums = [list(map(int, input().split()))for _ in range(N)]
    # print(nums) # 맨 왼쪽 위 에서 맨 오른쪽 아래 그 중 최소 합계
    kkk = 9876543210 # 최소 찾을 것
    ans(0,0,0) # 호출 한번 -> kkk 바뀔거임
    # print(ans(0,0,0))
    print(f'#{t} {kkk}') # 정답
