T = int(input())
for t in range(1,T+1):
    N = float(input())
    # print(2**(-1))
    val = N
    ssum = []
    for i in range(1,13):
        ssum.append((2**(-i)))
    # print(ssum[2])
    sublist = []
    for i in range(1<<len(ssum)):
        sub = []
        for j in range(len(ssum)):
            if i & (1<<j):
                sub.append(ssum[j])
        if sum(sub) == val:
            sublist.extend(sub)
    if sublist:
        arr = [0]*12
        for i in sublist:
            k = ssum.index(i)
            arr[k] = 1

            # print(arr)
        print(f"#{t}", end=' ')
        for i in range(k+1):
            print(arr[i],end='')
        print()
    else:
        print(f'#{t} overflow')
    # print(sublist)