T = int(input())
for t in range(1,T+1):
    tc, rango = map(str, input().split())
    rango = int(rango)
    arr = input().split() # 'ZER', 'ONE', 꼴 저장

    comp_numbers = 'ZRO', 'TWO',

    for n in comp_numbers:
        # n : zro two thr
        for m in arr:
            # num = tc내부의 뭔가 뭔가
            if num == n:
                print(num, end = ' ')
    print() # 모든 반복 끝나고 줄바꿈

    # 아! 리스트 순서만 쓱싹 하면 정렬이고 나발이고...
