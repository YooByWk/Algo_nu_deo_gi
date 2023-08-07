T = int(input())
testC, rango = map(str, input().split())
pattern = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
K = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
ptdt = dict(zip(pattern,K))
print(ptdt)
ori = list(input().split())
# result = []
counts = [0] * 10
for n in ori:
    counts[ptdt[n]] += 1
print(counts)
# for i in counts:
#     counts[i+1] += counts[i]
# print(counts)