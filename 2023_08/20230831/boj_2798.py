import sys
input = sys.stdin.readline

def comb(n,r,sum):
    global S
    if r == 0:
        return



N,M = map(int,input().split())
card = list(map(int,input().split()))
S = 0
bit = [0] * N
comb(N,3,sum)
print(S)