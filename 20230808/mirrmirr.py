def mirror(lst):
    mirr = ''
    for i in lst:
        if i == 'b':
            mirr = 'd' + mirr
        elif i == 'd':
            mirr = 'b' + mirr
        elif i == 'p':
            mirr = 'q' + mirr
        elif i == 'q':
            mirr = 'p' + mirr
        else:
            mirr = i + mirr

    return mirr

T = int(input())
for t in range(1, T+1):
    st = input()
    print(f'#{t}', mirror(st))
