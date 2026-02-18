### 그대로 출력하기

# 첫 풀이
"""
EOF를 어떻게 처리할 것인가가 관건
-> EOF는 파일의 끝을 의미
-> S == None이 아니라, EOFError를 처리해야함
-> EOFError는 파일의 끝을 읽으려고 할 때 발생하는 예외
-> try except로 처리할 수 있음
"""
for _ in range(100):
    S = input()
    if S == None:
        break
    else:
        print(S)
"""
# input을 이용해서 푸는 방법

for _ in range(100):
    try:
        S = input()
        print(S)
    except EOFError:
        break

"""


# 두번째 풀이
"""
sys.stdin.readline()은 한 줄을 읽어서 문자열로 반환
-> read()와 readline()의 차이는 read는 파일의 끝까지 읽어서 문자열로 반환하고, readline은 한 줄을 읽어서 문자열로 반환
-> readline()은 파일의 끝을 만나면 빈 문자열을 반환
-> 따라서, 빈 문자열을 처리하거나 sys.stdin.read()를 사용해야함
"""
import sys
S = sys.stdin.readline()
print(S)
"""
import sys

While True:
    data = sys.stdin.readline()
    # 빈 문자열은 bool 취급되므로 not data는 True가 되어 break
    if not data:
        break
    print(data)
"""


# 세번째 풀이
"""
repr()은 문자열의 실제 내부 표현(escape 포함) 을 보여주는 함수
-> repr()은 디버깅에 사용하는 함수이므로 개행문자도 그대로 string으로 출력됨
"""
import sys
data = sys.stdin.read()
print(repr(data))


# 정답풀이
import sys
data = sys.stdin.read()
print(data)
# or sys.stdout.write()를 사용하는 방법
import sys
data = sys.stdin.read()
sys.stdout.write(data)