N = 5
M = 4
arr = [[1,2,3,4],[4,3,2,1],[4,5,6,7],[4,5,6,7],[4,5,6,7]]
for r in range(N):
    sumV  = 0
    for c in range(M):
        sumV += arr[r][c]
    print(sumV)

sr,sc =1,0
sizeR = 2
sizeC= 3
sumV = 0
for r in range(sr, sr+sizeR):
    for c in range(sc, sc + sizeC):
        sumV += arr[r][c]
print(sumV)