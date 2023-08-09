T = int(input())
Gen = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for t in range(1, T+1):
    TC_NUM, rango = map(str, input().split())
    rango = int(rango)
    Earth = []
    lista = list(map(str, input().split()))
    for i in lista:
        for j in range(10):
            if i == Gen[j]:
                i = j
                Earth.append(i)
    for i in range(rango-1, 0 ,-1): # 버블정렬
        for j in range(0,i):
            if Earth[j]>Earth[j +1]:
                Earth[j],Earth[j+1] = Earth[j+1],Earth[j]
    lista2 = []
    for i in Earth:
        for j in range(10):
            if i == j:
                i = Gen[j]
                lista2.append(i)
    print(f'#{t}')
    print(*lista2)
