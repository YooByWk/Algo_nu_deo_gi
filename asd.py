# 테스트 케이스를 입력받는다
T = int(input())
print('T', T)
# 테스트 케이스만큼 반복한다
for tc in range(1, T + 1):  # +1? 결과 출력할 때 편하려고...
    print(f'#{tc}')
    # 테스트케이스 별로 12장의 카드 순서 정보를 전달 받는다. (order)
    order = list(map(int, input().split()))
    print('order', order)
    # 플레이어별로 가지고 있는 카드 번호별 장수를 나타내는 리스트를 만든다. (p1, p2)
    p1 = [0] * 10  # 0 ~ 9
    p2 = [0] * 10  # 카드번호별 장수를 카운트 -> 순서가 상관 X
    # 숫자인덱스(i)를 통해 반복문으로 order를 탐색한다.
    for i in range(len(order)):
        print('i', i)
        # 두 플레이어한테 교차하면서 한 장씩 넘긴다
        # i가 0, 2, 4, … 짝수이면 p1에 해당 숫자 카드(card)를 +1 한다.
        card = order[i]
        print('card', card)
        # if i % 2 == 0:  # i가 짝수일 때
        if not i % 2:  # i % 2 -> 0, 1 -> 0이 나오면 -> False -> Not False
            p1[card] += 1  # 1장을 (플레이어의 해당 인덱스) 위에 추가시켜줌
        # i가 1, 3, 5, … 홀수이면 p2에 해당 숫자 카드(card)를 +1 한다.
        if i % 2:  # if i % 2 == 1: # i가 홀수일 때
            p2[card] += 1

        # TODO : 어느쪽이든 카드가 늘어난 순간 triplet이나 run을 검사한다.
        # triplet → p1 또는 p2를 순서