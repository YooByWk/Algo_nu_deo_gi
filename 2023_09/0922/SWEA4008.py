# 4008. [모의 SW 역량테스트] 숫자 만들기
# 연산자 정리
# op = ["+", "-", "*", "/"]
import math
def cal(idx, op, value):
    global maxV, minV
    # print(value, end = '  ')
    if idx == N:
        maxV = max(maxV, value)
        minV = min(minV, value)

    if op[0]:
        op[0] -= 1
        cal(idx + 1, op, value + nums[idx])
        op[0] += 1

    if op[1]:
        op[1] -= 1
        cal(idx + 1, op, value - nums[idx])
        op[1] += 1

    if op[2]:
        op[2] -= 1
        cal(idx + 1, op, value * nums[idx])
        op[2] += 1

    if op[3]:
        op[3] -= 1
        cal(idx + 1, op, math.trunc(value / nums[idx]))
        op[3] += 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 각 연산자의 개수
    # + - * /
    op = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    maxV = -99999999
    minV = 99999999
    cal(1, op, nums[0])
    # print(maxV)
    # print(minV)
    # if minV < 0:
    #     print ('tc',tc)
    print(f'#{tc} {maxV - minV}')
