# 하샤드 수

"""
<문제 설명>
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

<제한사항>
x는 1 이상, 10000 이하인 정수입니다.

<입출력 예>
x	return
10	true
12	true
11	false
13	false

<입출력 예 설명>

"""

# 제시 코드
"""
def solution(a, b):
    answer = 0
    return answer
"""

# 풀이 코드
def solution(x):
    answer = True
    x_list = list(str(x))
    s = 0
    for i in x_list:
        s += int(i)
        
    if x % s == 0:
        answer = True
    else:
        answer = False

    return answer

# 더 간단히
def solution2(x):
    return x % sum(map(int, str(x))) == 0

# 회고
"""
1.
x % 각 자리 숫자를 더한 수 == 0 -> True이므로 
x % 각 자리 숫자를 더한 수 == 0 -> 이것만 return해도 됨

2. 
해야할 일은 1) digit_sum을 구하기, 2) 0인지 판별

3.
자릿수 합은 보통 str로 바꾸고 -> str(x)
문자열을 다시 int로 바꾸고 -> int(d)
다 더하기 -> sum(...)

-> sum(int(d) for d in str(x))

================================================================
total = 0
for d in str(x):
    total += int(d)
----------------------------------------------------------------    
이 형태는 거의 항상 아래로 축약 가능:

“누적합”이면 → sum(...)

“누적 리스트 만들기”면 → list comprehension / generator

“조건 필터”면 → if in comprehension / filter
================================================================

4. 
따라서, total = sum(int(d) for d in str(x))

5.
조건을 조립하면, return x % sum(int(d) for d in str(x)) == 0

6. map 버전
sum(map(int, str(x)))
return x % sum(map(int, str(x))) == 0

"""