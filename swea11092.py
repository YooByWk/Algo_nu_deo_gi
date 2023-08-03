T = int(input())
for t in range(1, T+1):
    el = int(input())
    lista = list(map(int, input().split()))
    minimo = 0
    maximo = 0
    for i in range(1, el):
        if lista[minimo] > lista[i]:
            minimo = i
        if lista[maximo] <= lista[i]:
            maximo = i
    k = abs(maximo - minimo)
    print(f'#{t} {k}')


