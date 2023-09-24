# 5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기
# 같은 조 만들고, 몇개의 조가 되는가
# 1~N 까지의 출석번호, M장의 신청서
# T // N, M // M 쌍

def find_set(x):
    if people[x] == x:
        return x
        # 경로 압축
    return find_set(people[x])

def union(x,y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        people[y] = x
    else:
        people[x] = y



T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    people = [i for i in range(N+1)]
    paper = list(map(int, input().split()))
    for i in range(0,M):
        union(paper[2*i], paper[2*i+1])

    # for i in range(1,N+1):
    #     find_set(people[i])
    # print(check)
    ans_set = set()
    for i in range(1,N+1):
        ans_set.add(find_set(i))
    # print(ans_set)
    ans = len(ans_set)
    print(f'#{t} {ans}')
