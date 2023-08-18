# 미로
"""
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000
#1 5
#2 5
#3 0
"""
# 변수 이름을 잘 사용합시다. . .
# 변수 이름이 길어지면 느려지나 궁금했습니다.
# 그리고 주석이 많으면 느려지는지도 궁금했습니다.

def Donde_esta_el_lugar_que_vamos_a_empezar_ya_vamos_a_buscar(): # 위치찾기


    for r in range(N):

        for c in range(N): # 찾아조

            if Joan_Miro_es_un_pintor_de_barcelona_y_me_gustan_mucho_sus_obras_debia_verlo_pero_no_lo_hice[r][c] == 2: # 살려조

                return r, c # 살려조




def bfs_de_Pablo_picaso_el_que_quiere_irse(stR,stC): # bfs 하기


    vsted = [[0] * N for _ in range(N)]
    queueueueueueueueueueueueueueueueueueueueueueup = []
    queueueueueueueueueueueueueueueueueueueueueueup.append((stR, stC))
    vsted[stR][stC] = 1

    while queueueueueueueueueueueueueueueueueueueueueueup:
        r,c =queueueueueueueueueueueueueueueueueueueueueueup.pop(0);
        if Joan_Miro_es_un_pintor_de_barcelona_y_me_gustan_mucho_sus_obras_debia_verlo_pero_no_lo_hice[r][c] == 3:
            return vsted[r][c]-2;
        for dr, dc in [[0,1],[1,0],[-1,0],[0,-1]]: # drdc drdc nr nc ?
            nr = c + dc #           zzzzzzzzzzz
            nc = r + dr # zzzzzz

            if 0 <= nc < N and 0 <= nr < N and Joan_Miro_es_un_pintor_de_barcelona_y_me_gustan_mucho_sus_obras_debia_verlo_pero_no_lo_hice[nc][nr] != 1 and  vsted[nc][nr] == 0 :
                queueueueueueueueueueueueueueueueueueueueueueup.append((nc,nr))
                vsted[nc][nr] = vsted[r][c] + 1
    return 0





T = int(input()) # 테 케

for tescase_will_print_the_number_of_testcase_wow_entonce_asi_sera_largo in range(1,T+1):

    N = int(input()) # N 줄
    Joan_Miro_es_un_pintor_de_barcelona_y_me_gustan_mucho_sus_obras_debia_verlo_pero_no_lo_hice = [list(map(int, input()))for _ in range(N)] # 미로 리스트
    # print('yeheyeyey')
    StartR, sTaRtC = Donde_esta_el_lugar_que_vamos_a_empezar_ya_vamos_a_buscar() # 찾은것
    la_clave_de_este_problma_sera_esto_espero_que_sea_la_clave_clara_por_favor = bfs_de_Pablo_picaso_el_que_quiere_irse(StartR, sTaRtC)
    print(f'#{tescase_will_print_the_number_of_testcase_wow_entonce_asi_sera_largo} {la_clave_de_este_problma_sera_esto_espero_que_sea_la_clave_clara_por_favor}')
