# 후위순회해서 답 도출
def postorder(t):
    if t:
        # 왼쪽
        postorder(c_left[t])
        # 오른쪽
        postorder(c_right[t])
        # t에서 방문처리
        result =


T = 1
for tc in range(1, T+1):
    n = int(input()) # 정점의 개수
    info = [0] * (n+1)
    c_left = [0] * (n+1)
    c_right = [0] * (n+1)
    for i in range(n): # 정점 개수 만큼 반복
        temp = list(input().split())
        for c in range(len(temp)):
            if temp[c].isdigit():
                temp[c] = int(temp[c])

        print(f"temp = {temp}")
        if type(temp[1]) == int: # 정점이 정수인 경우/ 정점 번호, 양의 정수
            info[temp[0]] = temp[1]
        else: # 정점이 연산자인 경우/ 정점 번호, 연산자, 왼쪽 자식 정점 번호, 오른쪽 자식 정점 번호
            info[temp[0]] = temp[1]
            c_left[temp[0]] = temp[2]
            c_right[temp[0]] = temp[3]



