

# T = int(input())
# # info of colours
# for t in range(1, T+1):
#     paper = [[0]*10 for _ in range(10)]
#     N = int(input())
#     for col in range(N):
#         X1, Y1, X2, Y2, Colour = map(int, input().split()) # to C, 1 means Red, 2 means Blue / no dupted
#         for r in range(X1, X2+1):
#
#             for c in range(Y1 , Y2 + 1):
#                 paper[r][c] += Colour
#     cnt = 0
#     for r in range(10):
#         for c in range(10):
#             if paper[r][c] == 3:
#                 cnt += 1
#     print(f'#{t}',end = ' ' )
#     print(cnt)
# '''


#돚 거
T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # N은 칠할 영역의 개수 # 색칠 횟수
    color_arr = [list(map(int, input().split())) for _ in range(N)] # 색칠 정보 구해오기
    zeros_arr = [[0] * 10 for _ in range(10)] # 백지 리스트
    count_ = 0 #여기서 정의 안하면 큰일나요
    print((color_arr))
    # 색깔 별로 모서리 부터 모서리 까지 색을 칠해준다
    # [0-r1,1-c1,2-r2,3-c2,4-Colour]
    for i in range(N):
        start_row = color_arr[i][0] #
        end_row = color_arr[i][2] #
        start_col = color_arr[i][1] #
        end_col = color_arr[i][3] #
        color = color_arr[i][4] #
        # [i] 뒤의 값은 고정임. 각 자리별로 의미는 다음과 같다.
        #col_arr [i][0] = r1
        #col_arr  [i][1] = c1
        #col_arr [i][2] = r2
        #col_arr [i][3] = c2
        #col_arr [i][4] = colour
        # i의 의미는 각 R이 한 색깔의 색칠 정보 (r1,c1,r2,c2,Colour를 담고 있기 때문에 색칠 횟수를 의미하는 N 만큼의 반복으로
        # 색칠할 정보를 가진 row 를 불러온다.
        # N이 2고, 값이 2 ,2, 4, 4, 1 / 3, 3 ,6, 6, 2 라면
        # col_arr은 [[2, 2, 4, 4, 1]
        #           [3, 3, 6, 6, 2]] 모양의 의 2차원 배열이다.
        for r in range(start_row, end_row + 1): # 위에서 받은 정보 0, 2  (r값)
            for c in range(start_col, end_col + 1): # 위에서 받은 1,3 (c값)
                zeros_arr[r][c] += color # Colour 값을 [[0] * 10 for _ in range(10)] (0 / 백지 인 전체 범위에 더함)
    for z_r in range(10): # 10
        for z_c in range(10): # 10 x 10
            if zeros_arr[z_r][z_c] == 3: # 색깔의 합이 3이라면 겹쳐진 부분이므로,
                count_ += 1  #카운트를 1 더해준다.
    print(f"#{tc} {count_}") # 끝!