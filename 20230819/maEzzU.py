T = int(input())
for t in range(1,1+T):
    maEJu = int(input())
    q = []
    nuGye = 0
    saRam = 1
    # 사람 번호, 마이쮸 개수
    while nuGye < maEJu:
        q.append([saRam, 0])
        saRam += 1
        inGan = q.pop(0)
        inGan[1] += 1
        nuGye += inGan[1]
        q.append(inGan)
    print(f"#{t} {inGan[0]})
