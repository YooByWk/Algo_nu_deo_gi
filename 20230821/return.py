T = int(input())
for t in range(1 + T):
    N = int(input())  # 돌아가야 할 학생의 수
    cor = [0] * 401
    stu = []
    sec = 0
    for i in range(N):
        a, b = map(int, input().split())
        stu.append([a, b])
    #########################
    while stu:
        sec += 1
        temp = stu.pop()
        for i in stu[::-1]:
            print(i,'i')
            print(temp,'t')
            if temp[1] > i[0]:
                temp = stu.pop()
                # continue
            elif temp[1] < i[0]:
                continue
                # temp = stu.pop(0)
    print(sec)
    뭐 잘 생각해보자고.
