# 0과 1로 이루어진 1차 배열에서 7개 byte를 묶어서 10진수로 출력하기
bit = "0000000111100000011000000111100110000110000111100111100111111001100111"
n = len(bit)
# 이진수를 7칸 쪼개서 십진수로 만들기
temp = []
answer = []
for i in range(0,n,7):
    temp.append(list(map(int, bit[i:i+7])))
for i in temp:
    n = 1
    for k in range(6,-1,-1):
        i[k] = i[k]*n
        n *= 2
for i in range(n//7):
    sum = 0
    for j in range(7):
        sum += temp[i][j]
    answer.append(sum)

print(*answer)
################
def bins(bi):
    print(bi):
    result =0
    for c in bi:
        result = result*2 +int(c)
    return result

s = '0000000111100000011000000111100110000110000111100111100111111001100111'
for i in range(0,len(s),7):
    print(bins(s[i:i+7]))
