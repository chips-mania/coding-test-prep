# 두 정수 사이의 합

"""
<문제 설명>
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

<제한사항>
a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
a와 b의 대소관계는 정해져있지 않습니다

<입출력 예>
a	b	return
3	5	12
3	3	3
5	3	12

<입출력 예 설명>

"""

# 제시 코드
"""
def solution(a, b):
    answer = 0
    return answer
"""

# 풀이 코드
def solution(a, b):
    answer = 0
    
    if a < b:
        while a < b:
            answer += a
            a += 1
        answer += b
    
    elif a > b:
        while a > b:
            answer += b
            b += 1
        answer += a
        
    else:
        answer = a
    
    return answer

# 더 간단히
def solution2(a, b):
    lo, hi = sorted((a, b))
    return (hi - lo + 1) * (lo + hi) // 2

# 회고
"""
a, b 순서 상관없이 정수 합이라서 등차수열 합 공식으로 끝낼 수 있음
"""