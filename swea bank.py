# 은행 업무
for t in range(1,int(input())+1):
    # N = int(input())
    bi = list(input())
    tri = list(input())
    b = []
    tl = []
    for i in range(len(bi)):
        tb = bi[:]
        #
        # if i == '0' and bi[i] != '1' :
        #     continue
        if bi[i] == '0':
            tb[i] = '1' # 일단 바꿔줌
            if tb[0] == '0' or ''.join(tb) == ''.join(bi):
                continue
            b.append(''.join(tb))
            tb[i] = '1'
        else:
            tb[i] = '1'
            tb[i] = '0'
            if tb[0] == '0' or ''.join(tb) == ''.join(bi):
                continue
            b.append(''.join(tb))
            tb[i] = '0'

    for i in range(len(tri)):
        tt = tri[:]

        if tri[i] =='0':

            tt[i] = '1'
            if tt[0] == '0' or ''.join(tt) == ''.join(tri):
                continue
            tl.append(''.join(tt))

            tt[i] = '2'
            if tt[0] == '0' or ''.join(tt) == ''.join(tri):
                continue
            tl.append(''.join(tt))

            tt[i] = '0'


        elif tri[i] =='1':
            tt[i] = '0'
            if tt[0] == '0' or ''.join(tt) == ''.join(tri):
                continue
            tl.append(''.join(tt))


            tt[i] = '2'
            if tt[0] == '0' or ''.join(tt) == ''.join(tri):
                continue
            tl.append(''.join(tt))

            tt[i] = '1'

        elif tri[i] == '2':

            tt[i] = '1'
            if tt[0] == '0' or ''.join(tt) == ''.join(tri):
                continue
            tl.append(''.join(tt))

            tt[i] = '0'
            if tt[0] == '0' or ''.join(tt) == ''.join(tri):
                continue
            tl.append(''.join(tt))

            tt[i] = '2'

    # print((b))
    # print((tl))
    b = set(b); tl=set(tl)
    b = list(b); tl = list(tl)
    for i in range(len(b)):
        for j in range(len(tl)):
            bin = int(b[i],2)
            ttr = int(tl[j],3)
            # print(bin,'b')
            # print(ttr)
            exit = 0
            if bin == ttr:
            # if int(b[i],2) == int(tl[j],3):
                print(f'#{t} {bin}')
                exit = 1
                break
        if exit == 1:
            break

