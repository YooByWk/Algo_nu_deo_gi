T = int(input())
for t in range(1,T +1 ):
    board, vez = map(int, input().split())
    board = list(str(board))
    n = len(board)
    temp2 = board[:]
###############################
    temp2 = ''.join(board)
    trash = [temp2]
    for asdf in range(vez):
        for tt in trash : # 2차원 배열 로동용
            ls = list(tt)
            for i in range(n-1): # 조합을 구하는 친구
                for j in range(i+1, n): # 조합을 구하는 친구
                    ls[i], ls[j] = ls[j], ls[i]
                    # if ''.join(tt) in trash:
                    if ''.join(ls) not in trash:
                        trash.append(''.join(ls))
                    ls[i], ls[j] = ls[j], ls[i]
    ans = []
    for i in trash:
        ans.append(''.join(i))
    ans.sort()

    print(f'#{t} {ans[-1]}')
# print(test)
# print(len(test))
 ####    ####    ####    ####    ####    ####    ####
   ####    ####    ####    ####    ####    ####   ####
    ####    ####    ####    ####    ####    ####    ####
     ####    ####    ####    ####    ####    ####    ####
      ####    ####    ####    ####    ####    ####    ####
