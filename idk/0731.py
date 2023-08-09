N = int(input())
arr = list(map(int, input().split()))
print(arr)

T = int(input())
for t in range(1,T+1):
    k, n, m = map(int, input().split())
    # k 충전 전 최대거리, n 종점,  m 충전기 수
    estacion = [0] # 정거장 리스트
    carga = list(map(int, input().split())) #충전소 위치
    estacion.extend(carga) # 중간 숫자
    estacion.append(n) # 종점 숫자
    distancia = 0 # 버스 이동거리
    estado = 0 # 현재위치
    ####################
    for i in range(len(estacion)-2):
        if estacion[i+2] - estado <= k:
            estado = estacion[i+2]
            print(estado, '장소')
            distancia += 1
        elif estacion[i+1] - estado <= k:
            estado = estacion[i+1]
            print(estado,'장소elif')
            distancia += 1
        else:
            distancia = 0
            print(f'#{t} 0')
            break
    if distancia != 0:
        print(f'#{t} {distancia}')
