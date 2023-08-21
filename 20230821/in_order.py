

def print_tree(root):
    global ans
    if root > N:
        return
    print_tree(root*2)
    ans += (arr[root])
      # 오른쪽이 tree 라면
    print_tree(root*2+1)

T = 10
for t in range(1, T+1):
    N = int(input()) # 트리의 정점의 수
    # 정점 번호, 해당 정점의 문자  ,왼쪽 자식번호, 오른쪽 자식번호
    arr = [0] * (N+1)
    temp = []
    idx = 0
    ans = ''
    # temp.append(0)
    for i in range(1,N+1):
        temp.append(list(input().split()))
    # print_tree(1)
    ix = 0
    for i in temp:
        arr[int(temp[ix][0])] = temp[ix][1]
        ix += 1
    print(arr)
    print_tree(1)
    print(f'#{t} {ans}')
