# 퀵 정렬
def h_part(s, e):
    p = s # pv
    i = s # i
    j = e # j
    while i <= j:
        while i <= j and lst[i] <= lst[p]:
           i += 1
        while i <= j and lst[j] >= lst[p]:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]

    lst[p], lst[j] = lst[j], lst[p]
    return j


def quick(s,e):
    if s >= e:
        return
    pv = h_part(s,e)
    quick(s, pv-1)
    quick(pv+1, e)

T = int(input())
for t in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))

    quick(0,N-1)
    print(f'#{t} {lst[N//2]}')