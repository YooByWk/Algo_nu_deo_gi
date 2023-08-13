T = int(input())
for t in range(1,T+1):
    N = int(input())
    Go = [list(map(int, input().split()))for _ in range(N)]
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    blackout = 0
    an_SSeuni_ka_byuensu_name_wan_jengilgae,mun_jae_rul_zal_ilk_jja_ze_bal_ao_na_mo_ham_jin_cha_queestoyhaciendoaquiparanousaresteobjetoahorajugandoconsunombre = map(int, input().split())
    for r in range(N):
        for c in range(N):
            cnt = 0
            kill = 0
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if Go[r][c] == 0:
                    if 0 <= nr < N and 0 <= nc < N:
                        if Go[nr][nc] == 2:
                            # cnt += 1
                            white = 0
                            for j in range(4):

                                kr = nr + dr[j]
                                kc = nc + dc[j]
                                if 0 <= kr < N and 0 <= kc < N:
                                    if Go[kr][kc] == 1:
                                        white += 1
                            if white == 3:
                                kill += 1

            if blackout < kill:
                blackout = kill

    print(f"#{t} {blackout}")
