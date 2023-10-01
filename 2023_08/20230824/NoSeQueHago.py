def dtob(n):
    res = ''
    for c in range(4):
        t = n & (1<<c):
        if t != 0:
            res += '1'
        else:
            res += '0'
    return res
print(dtob(10))
