num = '01D06079861D79F99F'
# '01D0607 9861D79 F99F'
res = 0
# 7 단위 슬라이싱 해야함
N = len(num)
print(len(num))
for i in range(0,N,7):
    temp =[]
    res= 0
    for j in range(i,i+7):
        if i + 7 > N:
            temp = num[i:N]
        else:
            temp = num[i:i+7]
    for c in temp:
        if c.isalpha():
            res += res * 16 + ord(c)-ord('A') + 10
        else:
            res += res * 16 + int(c)
    # print(temp)
    print(res)
