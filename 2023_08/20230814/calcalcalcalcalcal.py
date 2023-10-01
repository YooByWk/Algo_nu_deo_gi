'''
6528-*2/+
'''
stack = [0] * 100
top = -1
s = '6528-*2/+'
for x in susik:
    if x not in '+-*/': # 피연산자라면
        top += 1
        stack[top] = int(x)
    else:
        op1 = stack[top]
        top -= 1
        op2 = stack[top]
        top -= 1
        if x == '+':
            stack[top] = op1 + op2
        elif x =='-':
            stack[top] = op1 - op2
        elif x == '/':
            stack[top] = op1 / op2
        elif x == '*':
            stack[top] = op1 * op2

