T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lista = list(map(int, input().split()))

    for i in range(n-1,0,-1): # i 구간의 마지막 idx. n-1(마지막 자리 인덱스)부터 0까지 , 감소하면서
        for j in range(i): #
    # 추측 1 : 두개의 for가 필요한 이유는 한번만 돌면 b c a d e 가 b a c d e 가 될거임...
        # 그러니까 한번 더 돌립니다.
            if lista[j] > lista[j+1]: # 오름차순이니까 크기 비교
                lista[j], lista[j+1] = lista[j+1], lista[j] # 크면 이거 해라

    print(f'#{tc}', *lista) #  unpacking

