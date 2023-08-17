# 비밀번호 한번....
for _ in range(1, 11):
    t = int(input())
    nums = list(map(int, input().split()))
    # 1 2 3 4 5 감소함
    while nums[-1] != 0: # 0과 같으면 못나온다.
        for i in range(1, 6): # 한사이클
            k = nums.pop(0)
            k -= i
            if k <= 0:
                k = 0
                nums.append(k)
                print(f'#{t}', *nums)
                break
            nums.append(k)
