# def ans(M):
#     res = ''  # 결과용 문자
#     alp = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15} # 10진법 dict
#     for i in M:
#         temp ='' # 임시 저장용 문자
#         cnt = 0 # while 탈출용 / 2 > 16 4글자
#         if i in alp:  # 숫자인지 알파벳인지 보고
#             k = alp[i]  #알파벳이라면 숫자로 바꿔주기
#         else:
#             k = int(i) # str -> int
#         while cnt != 4: # 0, 1, 2, 3
#             n = k % 2  #나머지
#             temp =  str(n) + temp # 를 더하고
#             k //= 2  #다음 값은 2로 나눈 것
#             cnt +=1  # 자리수 1개 했읍니다.
#
#         # if len(temp) % 2 ==1:
#         #     temp = '0' + temp
#         res = res + temp
#     return res
#
#
# T = int(input())
# for t in range(1,T+1):
#     N,M = input().split()
#     alp = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
#     # 1010,1011,1100,1101,1110,1111
#     # print(alp['A'])
#     res = ''
#     print(f'#{t} {ans(M)}')
#     # print(bin(alp['A']))
#     # print(bin(alp['B']))
#     # print(bin(alp['C']))
#     # print(bin(alp['D']))
#     # print(bin(alp['E']))
#     # print(bin(alp['F']))


def decToBin(dec):
   # 비트연산을 사용해보자?
   res =''
   for cnt in range(int(N)*4):
       t = dec & (1<<cnt)
       if t != 0:
           res = '1' + res
       else:
           res = '0' + res

   return res

def hexTodec(hx): # 이름 잘못됨 hx to dec 임
    res = 0
    for c in hx:
    # 10A
        if c.isalpha():
            t = ord(c) - ord('A') + 10
            res = res * 16 + t
        else:
            res = res * 16  +  int(c)
    return res


def hxtobin(hx):
    res = ''
    return decToBin(hexTodec(hx))


T = int(input())
for t in range(1,T+1):
    N,M = input().split()
    print(f'#{t} {hxtobin(M)}')