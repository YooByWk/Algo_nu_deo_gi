# Swea 5208 전기버스
# ultima habitacion no tiene bateria
# T : test case
def bus(loc, bat, cnt):
    global _min

    if cnt >= _min:
        return

    # Parar
    # if loc >= N-1:
    #     if cnt < _min:
    #         _min = cnt
    #     return

    # Trabajo
    if loc + bat >= N - 1 and cnt < _min:
        _min = cnt
        return
    if bat != 0:
        bus(loc+1,bat-1,cnt)

    if cnt+1 < _min:
        bus(loc+1,stop[loc]-1,cnt+1)



## ## ## ## ## ## ## ## ## ## ## ##
T = int(input())
for t in range(1,T+1):
    # N(la cantidad de habitacion,
    # N-1 (bateria de cada habitacion),
    # M (volumen de bateria)
    N, *stop = list(map(int, input().split()))
    stop += [0]
    # print(stop)
    _min = 12312356673453456260 # para ver las veces del cambio de la bateria

    bus(0,stop[0],0)
    print(f'#{t} {_min}')