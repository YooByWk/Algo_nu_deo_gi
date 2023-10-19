
def insert(item):
    global last # 바깥 자리가 바뀐다.

    last += 1 # 마지막 자리
    heap[last] = item # 힙에 넣음
    cur = last # 자식 노드 # 현재 위치
    while cur > 1:
        prnt = cur // 2
        if heap[prnt] > heap[cur]:# 부모가 자식보다 크면... 안되니까...
            heap[prnt], heap[cur] = heap[cur], heap[prnt] # 바꿔요
            cur = prnt
        else:
            break


T = int(input())
for t in range(1,T+1):
    N = int(input())
    tmp = list(map(int,input().split()))


    # heap = [0] * (30 ) # 힙 준비하기  # 나 진짜 뭐함?
    heap = [0] * 1000009
    last = 0 # 들어있는게 없으니까
    for i in tmp:
        insert(i)  # 리스트 받아서 하나씩 할라구요
    something = N # 정답 구하기 위한 인덱스 전용 숫자 마련
    ans = 0 # 정답 저장소

    while something > 1: # 1일때 값은 아래에서 계산 후에 들어가는 것이라 문제 없습니다
        something = something // 2 # 완.이.나.2 == 부.모
        # heap[something] += ans # 나 뭐함..?
        ans += heap[something]  # 알죠 이제?
    if N == 1:
        ans = heap[1]
    # print(heap)
    print(f'#{t} {ans}')
