def f1(base, exp):
    if base  == 0 :
        return 1
    r = 1
    for i in range(exp):
        r *= base
        return r
def f2(b, exp):
    if b == 0 or exp == 0 :
        return   1
    if b%2: #홀수
        r = f2(b, (exp-1)//2) #
        return r * r  * b
    else: # 짝수
        r = f2(b, (exp - 1 ) // 2 )
        return r * r





print(f1(2, 10))
print(f2(2, 10))