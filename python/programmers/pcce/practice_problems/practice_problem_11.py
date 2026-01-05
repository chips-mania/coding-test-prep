# 숫자 짝꿍


"""
<문제 설명>
두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다(단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다). X, Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다. X, Y의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.

예를 들어, X = 3403이고 Y = 13203이라면, X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다. 다른 예시로 X = 5525이고 Y = 1255이면 X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552입니다(X에는 5가 3개, Y에는 5가 2개 나타나므로 남는 5 한 개는 짝 지을 수 없습니다.)
두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성해주세요.

<제한사항>
3 ≤ X, Y의 길이(자릿수) ≤ 3,000,000입니다.
X, Y는 0으로 시작하지 않습니다.
X, Y의 짝꿍은 상당히 큰 정수일 수 있으므로, 문자열로 반환합니다.

<입출력 예>
X	Y	result
"100"	"2345"	"-1"
"100"	"203045"	"0"
"100"	"123450"	"10"
"12321"	"42531"	"321"
"5525"	"1255"	"552"

<입출력 예 설명>

"""

# 제시 코드
"""
def solution(X, Y):
    answer = ''
    return answer
"""

# 풀이 코드
def solution(X, Y):
    answer = ''
    i_list = []
    for i in X:
        if i in Y:
            Y=Y.replace(i,"",1)
            i_list.append(i)
    
    if i_list==[]:
        answer = '-1'
    
    elif set(i_list) ==['0']:
        answer = '0'
    
    else:
        i_list.sort(reverse = True)
        num = 0
        num = int(''.join(map(str,i_list)))
        answer = str(num)
    
    return answer

# 더 간단히
def solution2(x):
    return x % sum(map(int, str(x))) == 0
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

# 회고
"""
기능은 하지만 너무 비효율적인 코드가 많음
축약한다고 무조건 좋은건 아니지만 요구에 맞게 간단하게 보여줄 필요가 있음
"""