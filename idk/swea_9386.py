# Swea 9386 연속한 1의 개수

T = int(input())
for t in range(1, T+1):
    rango = int(input())
    contado = 0
    lista = list(map(int, input()))
    # input().split()
    # print(lista)
    maximo = 0
    for i in range(len(lista)):
        if lista[i] == 1:
            contado += 1
            if maximo < contado:
                maximo = contado
        else:
            contado = 0
    print(f'#{t} {maximo}')