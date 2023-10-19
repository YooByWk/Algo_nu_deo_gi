# 처음으로 달라지는 구간에서 한번 이미 리스트에 있는지 확인한다.
# 없다면 추가하고 그 문자로 나아간다.
# 있다면 해당 반복문을 종료한다.
N = int(input())
ans = N
for t in range(N):
    test = input()
    ls= []
    cnt = 0
    for i in range(len(test)-1):
        if test[i] == test[i+1]:
            pass
        elif test[i] in test[i+1:]:
            ans -= 1
            break
print(ans)