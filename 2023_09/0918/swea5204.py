def merge(l,r):
    global cnt
    result = [] # 결과창입니다?
    lp = rp = 0
    if l[-1] > r[-1]:
        cnt += 1 # 왼쪽의 마지막이 오른쪽보다 클 때 경우의 수 하나 증가
    while lp < len(l) and rp< len(r):

        if l[lp] < r[rp]:
            result.append(l[lp])
            lp += 1 # 하나 넣었으니까 오른쪽으로 인덱스 하나
        else:
            result.append(r[rp])
            rp += 1 # 하나 넣었으니까 오른쪽으로 인덱스 하나
    result += l[lp:] # 비교가 끝난 후 남은 것을 넣는다.
    result += r[rp:] # 비교가 끝난 후 남은 것을 넣는다.
    return result
def merge_sort(lst):
    N = len(lst)
    if N == 1:
        return lst
    result = []
    m = N//2

    # L
    L_lst = merge_sort(lst[:m])
    # R

    R_lst = merge_sort(lst[m:])

    return merge(L_lst,R_lst)

###############
T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 병합 과정에서 다음처럼 왼쪽 마지막 원소가 오른쪽
    # 마지막 원소보다 큰 경우의 수를 출력한다.
    cnt = 0
    res = merge_sort(arr)
    print(f'#{t} {res[N//2]} {cnt}')