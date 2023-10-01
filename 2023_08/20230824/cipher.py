import sys
# sys.stdin = open('input.txt', 'r')
def decToBin(dec):
   # 비트연산을 사용해보자?
   if dec != '0':
       res =''
       for cnt in range(4):
           t = int( dec) & (1<<cnt)
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
    code[r][k] = res
    return resH


def hxtobin(hx):
    res = ''
    return decToBin(hexTodec(hx))

#################################################################
def find_code(lst):
    for r in range(N):
        for c in range(M):
            if lst[r][c] != '0':
                print(type(code[r][c]))
                print(lst[r][c])
                loc = code[r]
                return loc
def sub(kk):
    i = 0
    while kk[i] == '0':
        i += 1
    return code[i]
##############################################################
T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    code = [list(input()) for _ in range(N)]
    arr = []
    #16진 > 10 진