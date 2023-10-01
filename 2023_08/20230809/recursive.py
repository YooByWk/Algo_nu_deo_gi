def func3():
    print(3)
    return
def func2():
    func3()
    print(2)
    return
def func1():
    func2()
    print(1)
    return

func1()

# 팩토리얼
def factorial(n):
    if n == 1:
        return 1
    result = n * factorial(n-1)  # 디버깅용
    return result

factorial(5)


########

def fib(n):
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    v1 = fib(n-1) #재귀
    v2 = fib(n-2) #재귀

    return v1 + v2

print(fib(40))

'''
'''
#memoization


def fib(n):
    if memo[n] != -1:
        return memo[n]

    # if n <= 1:
    #     return n

    v1 = fib(n - 1)  # 재귀
    v2 = fib(n - 2)  # 재귀
    memo[n] = v1 + v2
    return memo[n]


memo = [-1] * 151
memo[0] = 0
memo[1] = 1
print(fib(40))


