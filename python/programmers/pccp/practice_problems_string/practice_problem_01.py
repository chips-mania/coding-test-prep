# qr code


"""
<문제 설명>
두 정수 q, r과 문자열 code가 주어질 때, 
code의 각 인덱스를 q로 나누었을 때 나머지가 r인 위치의 문자를 앞에서부터 
순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

<제한사항>
0 ≤ r < q ≤ 20
r < code의 길이 ≤ 1,000
code는 영소문자로만 이루어져 있습니다.

<입출력 예>
q	r	code	result
3	1	"qjnwezgrpirldywt"	"jerry"
1	0	"programmers"	"programmers"

<입출력 예 설명>

"""

# 제시 코드
"""
def solution(q, r, code):
    answer = ''
    return answer
"""

# 풀이 코드
def solution(q, r, code):
    answer = ''
    str_lst =[]
    l = len(code)

    for idx in range(0,l):
        if idx%q == r:
            str_lst.append(code[idx])
    answer = "".join(str_lst)

    return answer

# 더 간단히
def solution(q, r, code):
    return code[r::q]
"""
* 문자열 슬라이싱

code[start:stop:step]
- start: 어디서부터 시작할지
- stop : 어디까지 자를지
- step : 몇칸씩 건너뛸지

* code[r::q]의 의미
- r부터 시작해서 끝까지, q칸마다 하나씩 return
- 즉, 인덱스가 r, r+q, r+2q, ... 인 문자들을 뽑아서 이어붙임

"""

# 회고
"""
문자열문제가 나오면 슬라이싱 고려
"""