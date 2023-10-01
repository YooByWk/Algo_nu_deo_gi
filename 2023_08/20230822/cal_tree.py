def calc(l,r,op):
    if op == '+':
        return l + r
    if op =='-':
        return l - r
    if op == '*':
        return l * r
    if op == '/':
        return l // r
def post(root):
    if tree[root][0].isdecimal():
        return int(tree[root][0])
    else:
        vl = post(int(tree[root][1]))  # 왼쪽
        vr = post(int(tree[root][2]))  # 오른쪽
        tree[root][0] = calc(vl, vr, tree)
        return calc(vl,vr,tree[root][0])

N = int(input())
tree = [[0,0] for _ in range(N+1)]
for i in range(N):
    s = list(input().split())
    nodeNo = int(s[0])
    tree[nodeNo] =  s[1::]

