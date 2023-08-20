for t in range(1, int(input())+1):
    pt = input()
    txt = input()
    N = len(pt)
    M = len(txt)
    i = 0
    j = 0
    while i < N and j < M:
        if pt[i] != txt[j]:
            j += 1 - i
            i = 0
        elif pt[i] == txt[j]:
            j +=1
            i+=1
    if i ==N:
        print(f'#{t} 1')
            # break
    else:
        print(f"#{t} 0")