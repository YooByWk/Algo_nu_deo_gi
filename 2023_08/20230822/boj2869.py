
A,B,V = map(int,input().split())
# A 미터를 낮에 올라가요
# B 밤에 미끄러져요
# V 정상가면 멈춰요
T = 0
if A > V:
    print(1)
elif (V-A) % (A-B) == 0:
    print((V-A) // (A-B) + 1)
else:
    print((V-A)//(A-B)+2)