import sys
input = sys.stdin.readline

st = []
K = int(input());sum=0;
for i in range(K):
    l = int(input())
    if l != 0 :
         st.append(l)
         sum += l
    else:
        sum -= st.pop()

print(sum)