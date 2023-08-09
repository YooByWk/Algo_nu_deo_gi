# swea 4843 특별한 정렬
def maX(lista):
    mmax = 0
    for i in lista:
        if i > mmax:
            mmax = i
    return  mmax

def maxidx(lista):
    mmax = 0
    idx = 0
    for i in range(len(lista)):
        if i > mmax:
            mmax = lista[i]
            idx = i
    return idx

def miN(lista):
    mmin = 110
    for i in lista:
        if i < mmin:
            mmin = i
    return mmin

def minidx(lista):
    mmin = 101
    idx = -1
    for i in range(len(lista)):
        if i < mmin:
            mmin = lista[i]
            idx = i
    return idx


T = int(input())
for t in range(1, T+1):
    n = int(input()) # n 개의 정수가 주어진다.
    a = list(map(int,input().split()))
    for i in range(n-1):
        mindx = i
        maxdx = i
        for j in range(i+1, n):
            if i % 2 == 0:
                if a[maxdx] < a[j]:
                    maxdx = j
                a[i], a[maxdx] = a[maxdx], a[i]
            else:
                if a[mindx] > a[j]:
                    mindx = j
                a[i], a[mindx] = a[mindx], a[i]
    print(f'#{t}', *a)

