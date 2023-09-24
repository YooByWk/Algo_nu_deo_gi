import sys
# 유클리드 호제법
N, M = map(int, sys.stdin.readline().split())
X = max(N,M)
Y = min(N,M)
a = ''
b = ''
for i in range(X):
    a += '1'
for i in range(Y):
    b += '1'
X = int(a)
Y = int(b)
# print(X,Y)
while X%Y:
    X, Y = Y, X%Y
print(Y)