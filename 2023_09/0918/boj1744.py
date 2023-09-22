T= int(input())
lst = []
for t in range(T):
    lst.append(int(input()))
lst.sort()
res = 0
new = []
if T == 1:
    print(lst[0])
elif T % 2 == 1: # 홀수
    for i in range(T-1,0,-2):
        if lst[i]*(lst[i-1]) >= 0 and lst[i] == 0:
            new.append(lst[i]*(lst[i-1]))
        else:
            new.append(lst[i])
            new.append(lst[i - 1])

else: # 짝수 케이스
    for i in range(T-1,-1,-2):
        # print(i)
        if lst[i]*(lst[i-1]) >= 0 and lst[i] == 0:
            # 분기를 바꿔서 0이랑 마이너스가 나오는 부분에서 다시. 해본다.
            # 아마 그러면 될 듯
            new.append(lst[i]*(lst[i-1]))
        else:
            new.append(lst[i])
            new.append(lst[i-1])
print(sum(new)) # git질 안됐네 하.