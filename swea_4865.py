
T = int(input())
for t in range(1, T+1):
     str1 = str(input())
     str2 = str(input())
     cntmx = 0
     for i in str1:
         cnt = 0
         if i in str2:
             for j in str2:
                 if i == j:
                     cnt +=1
         if cntmx < cnt:
             cntmx = cnt

     print(f'#{t} {cntmx}')