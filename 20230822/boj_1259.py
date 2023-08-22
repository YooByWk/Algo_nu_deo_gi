k = input()
while k != '0' :
    if k == k[::-1]:
        print('yes')
    else:
        print('no')
    k = input()
    # 팰린드럼수