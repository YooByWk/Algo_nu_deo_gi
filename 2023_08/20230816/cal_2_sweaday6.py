# import sys
# sys.stdin = open('input.txt')


T = 10
for tc in range(1, T+1):
    N = int(input())    # 계산식의 총 길이
    tokens = input()    # 계산식 (데이터 타입은 문자열!!!)

    # 후위 표기법
    # 필요한 것은 stack
    numbers = '0123456789'  # 숫자인지 확인하기 위한 문자열!
    stack = []
    postfix_notation = ''
    # 토큰을 하나씩 불러서 스택의 마지막 연산자와 비교해서 stack 에 넣을지 말지 정하자!!
    # 단 토근의 숫자는 바로 출력(새로운 문자열로 만들 것임!!)
    for token in tokens:
        # token 이 숫자라면 그대로 붙이고
        # token 이 연산자 라면 stack 과 비교할건데 (+ 밖에 없음)
        #  pop 후 push 를 할 것이다. (왜냐면 + 와 + 는 우선순위가 같기에 빼고 더하는 식으로 관리)
        if token in numbers:  # 토큰 값이 문자열에 있다면 => 숫자!!
            # 숫자는 바로 출력
            postfix_notation += token
        else: # 연산자 라면
            # + 연산자 밖에 없기 때문에
            # stack에 연산자가 있으면
            # * 는 stack의 top에 있는 친구가 * 라면 pop 하고 더하거나, 혹은 stack이 빌 때 까지 pop 한다.
            # token의 연산자가 stack의 연산자보다 커야 스택에 들어갈 수 있다.
            # 연산자 우선순위가 stack에 있는 것이 낮아질 때까지 계속 pop 해야한다.
            # stack이 비어 있다면 바로 append
            # 만약 + 연산자라면?
            # stack에 어떤 연산자가 들어 있더라도, 즉 본인보다 낮은 우선 순위가 없기에 항상 stack이 빌 때까지 pop해야 한다.
            if token == '*':
                while stack[-1] != '+' or len(stack) != 0:
                    postfix_notation += stack.pop()

            elif token == '+':
                while len(stack) != 0:
                    postfix_notation += stack.pop()
                stack.append()

            if len(stack) == 0:  # ? 어떻게 평가될까요??  빈 리스트라면? False 하나라도 있으면 True
                # 최대한 코드는 명시적인 것이 좋다! 팀원들이 내 코드를 봐도 이해하기 빠르기 때문!!
                stack.append(token)
            else:
                # 스택에 연산자가 있으면 빼서 출력하고
                tmp = stack.pop()
                postfix_notation += tmp
                # 토큰의 연산자를 스택에 넣는다.
                stack.append(token)

    # 모든 토큰 확인이 끝나면 stack에 남은 1개의 연산자를 출력해준다.
    while len(stack):
        postfix_notation += stack.pop()

    # print(postfix_notation)  # 후위 연산자 변환 끝!!

    # 이제 계산하자!!
    # 숫자를 stack 넣고! 연산자가 오면 두 개를 꺼내서 계산을 합시다!!
    stack = []
    result = 0
    for token in postfix_notation:
        if token in numbers:  # 이번에는 숫자를 push
            stack.append(token)
        else:
            # 숫자가 아닌 연산자라면 숫자 2개를 뽑아서 계산하자
            if token == '+':
                value2 = stack.pop()
                value1 = stack.pop()
                result = int(value1) + int(value2)
                # 계산이 끝나면 다시 스택에 push!
                stack.append(result)
            elif token == '*':
                    value2 = stack.pop()
                    value1 = stack.pop()
                    result = int(value1) * int(value2)
                    stack.append(result)

    print(f'#{tc} {stack.pop()}')