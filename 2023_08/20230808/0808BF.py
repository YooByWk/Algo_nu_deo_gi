# t안에 p가 존재하면 위치 return, 못찾으면 0 return
def brute(t, p):
    N = len(t)
    M = len(p)

    tp = 0  # text 위치
    pp = 0  # patt 위치
    while  tp < N and pp < M: #여기 조건으로 빠져나감. 패턴길이가 패턴포지션과 같아지거나, 못찾아서 전체길이 때문에
        if t[tp] != p[pp]:

            tp = tp - pp + 1
            pp = 0 # 자리 조심
        else:
            tp += 1
            pp += 1

    if pp == M:
        return tp - pp
    else:
        return -1
txt = 'TTTTAACCA'
pat = 'TTA'
print(brute(txt, pat))