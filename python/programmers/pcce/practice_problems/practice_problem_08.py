# 짝수와 홀수

"""
<문제 설명>
정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, 
solution을 완성해주세요.

<제한사항>
num은 int 범위의 정수입니다.
0은 짝수입니다.

<입출력 예>
num	return
3	"Odd"
4	"Even"

<입출력 예 설명>

"""

# 제시 코드
"""
def solution(price, money, count):
    answer = -1

    return answer
    
"""

# 풀이 코드
def solution(num):
    answer = ''

    if num % 2 == 1:
        answer = 'Odd'
    else:
        answer = 'Even'
        
    return answer


# 회고
"""
'//' -> 몫
% -> 나머지
기억해두기
"""