total = 20
Q = []
newH = 1
sumV = 0
cnt = 0
while sumV < total :
    print(Q,'while 시작')
    Q.append((newH, 1))
    newH += 1
    h, candy = Q.pop(0)
    sumV += candy
    Q.append((h, candy+1))
    cnt +=1
    print(Q,f'while {cnt}번째 진행 완료')

print(h,'가 아무튼 가져감')