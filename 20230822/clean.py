def deq():
    global last
    tmp = heap[1]                                   # 루트 백업
    heap[1] = heap[last]                            # 삭제할 노드의 키를 루트에 복사
    last -= 1                                       # 마지막 노드 삭제
    p =1                                            # 루트에 옮긴 값을 자식과 비교
    c = p * 2                                       # 왼쪽 자식
    while c <= last:                                # 자식이 하나라도 있다면. . . (비교할 자식노드 번호)
        if c +1 <= last and heap[c] < heap[c+1]:    # 오른쪽 자식 있고, 오른쪽 자식 더 크면
            c += 1                                  # 비교 대상이 오른쪽 자식 노드
        if heap[p] < heap[c]:                       # 자식이 더 크면 최대힙 규칙에 어긋난다.
            heap[p], heap[c] = heap[c], heap[p]
            p = c                                   # 자식을 새로운 부모로
            c = p * 2                               # 왼쪽 자식 번호를 계산
        else:                                       # 부모가 더 크 면
            break                                   # 비교 ㄱ중단




    return tmp


heap = [0] *100
