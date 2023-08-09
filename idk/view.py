# I hate you View.
def my_max(x, y, a, b):
    temp = [x, y, a, b]
    cur_max = temp[0]
    for i in temp:
        if cur_max < i:
            cur_max = i
    return  cur_max

for t in range(1,11):
    # 가로 1000 이하, 양 옆 두칸은 비어있다.
    n = int(input()) # 건물의 수
    piso = list(map(int, input().split())) #건물의 리스트
    suma = 0
    for i in range(2,  n-2):
        # print(i,'------------')
        dif = my_max(piso[i - 2], piso[i - 1], piso[i + 1], piso[i + 2])
        # print(dif,'dif')
        # if piso[i] > dif:
        V = piso[i] - dif
        # print(V, 'V')
        if V < 0 :
            V = 0
        suma += V
        # print(suma, 'sum')
    print(f'#{t} {suma}')

