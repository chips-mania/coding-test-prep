# qr code


"""
<문제 설명>
숫자로 이루어진 문자열 t와 p가 주어질 때, t에서 p와 길이가 같은 부분문자열 중에서, 이 부분문자열이 나타내는 수가 p가 나타내는 수보다 작거나 같은 것이 나오는 횟수를 return하는 함수 solution을 완성하세요.

예를 들어, t="3141592"이고 p="271" 인 경우, t의 길이가 3인 부분 문자열은 314, 141, 415, 159, 592입니다. 이 문자열이 나타내는 수 중 271보다 작거나 같은 수는 141, 159 2개 입니다.

<제한사항>
1 ≤ p의 길이 ≤ 18
p의 길이 ≤ t의 길이 ≤ 10,000
t와 p는 숫자로만 이루어진 문자열이며, 0으로 시작하지 않습니다.

<입출력 예>
t	p	result
"3141592"	"271"	2
"500220839878"	"7"	8
"10203"	"15"	3

<입출력 예 설명>

"""

# 제시 코드
"""
def solution(t, p):
    answer = 0
    return answer
"""

# 풀이 코드
def solution(t, p):
    answer = 0
    # cnt = 0
    for i in range(0, len(t)-(len(p)-1)):
        # print(p)
        # print(t[i:i+len(p)])

        if t[i:i+len(p)] <= p:
            # print("T")
            answer += 1
        # else:
            # print("F")
        # print("")
    
    return answer

# 더 간단히
def solution2(t, p):
    # p의 길이
    m = len(p)
    
    return sum(t[i:i+m] <= p for i in range(len(t) - m + 1))

"""
range(len(t) - m + 1)
->  t에서 길이가 m짜리 조각을 뽑을 수 있는 시작 인덱스 범위

for i in range(len(t) - m + 1)
-> 그 중 i를 뽑아서

t[i:i+m] <= p
-> t의 i부터 m개 글자를 잘라서 p와 비교
-> 출력은 True or False 조건식이 되고
-> 파이썬에서 True는 1, False는 0
-> 이 개수를 모두 sum


"""

# 회고
"""
list comprehension활용하면 컴팩트하게 표현가능
카운트에는 generator expression + sum으로 불필요한 리스트 생성을 피할 수 있음
"""