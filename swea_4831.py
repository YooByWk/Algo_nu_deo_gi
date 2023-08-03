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
    for i in range(len(carga)):
        if estacion
