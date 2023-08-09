#나는 숫자가 싫어요
T = int(input())
for t in range(1, T+1):
    n = int(input())
    num = input()
    numlist = list(map(int, num))
# print(numlist)
    canti = []
    canti = [0] * 10 # 0~9 까지니까요... 10개정도...
    max_can = canti[0]
    max_num = 0
    for i in numlist:
        canti[i] += 1
    print(canti)
    for j in range(1,10):
        if canti[j] >= max_can:
            max_can = canti[j]
            max_num = j
    print(f'#{t} {max_num} {max_can} ')