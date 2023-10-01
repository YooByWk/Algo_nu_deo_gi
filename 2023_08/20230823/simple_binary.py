# import sys
# sys.stdin = open("input99.txt", 'r')

def startR(lst): # 암호 탐색할 줄 번호
    for i in range(N):
        if '1' in lst[i]:
            return i

for t in range(1, int(input())+1):
    N,M = map(int,input().split())
    # N 줄 // M개 글자
    code = [] # 공배열
    for _ in range(N): # 아 str로 못받는 허접이라서 못했어요
        temp =input() # 인풋
        code.append(temp) # 너무 오랜 시간이 지나서 기억도 나지 않는다.
    # print(code)  #  암호코드의 길이는 56
    dcd = {
         '0001101': 0, '0011001': 1, '0010011':2,'0111101':3,
        '0100011':4, '0110001':5,'0101111':6,'0111011':7,'0110111':8,
        "0001011":9
    } # 나중에 사용할 딕셔너리
    sus = code[startR(code)]
    # print(str(sus))
    # 코드는 무조건 56글자다.
    # 1로 끝나지 않는 코드는 없다. 따라서 56번째는 무조건 1.
    i = sus[::-1]  #
    i = int(i)  # 0 제거하기 귀찮음.
    # print(i, type(i))
    i = str(i) # 슬라이싱을위해 문자열로
    i = i[0:56] # 쓱
    i = i[::-1] # 원래 모양대로 다시 뒤집어버림
    # print(i, 111111111111111111111111111111)
    even = [] # 리스트 1
    odd =[] # 리스트 2
    # 0111011 0110001 0111011 0110001 0110001 0001101 0010011 0111011
    for j in range(0,56,14):
        calc_even = ''
        calc_odd =  ''
        for k in range(j,j+7):
            calc_odd +=i[k]
            calc_even +=i[k+7]
        odd.append(dcd[calc_odd])
        even.append(dcd[calc_even])

    res = sum(odd)*3 + sum(even) # 결과 일단 출력
    if res % 10 == 0:
        print(f'#{t} {sum(odd)+sum(even)}')
    else:
        print(f'#{t} 0')
    # print(res) # 체크용
    # print(odd,even)  #체크용


    # print(start) # 실패의 흔적
